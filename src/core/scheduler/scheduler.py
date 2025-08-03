import asyncio
import sys
import threading
import time
from asyncio import AbstractEventLoop

import schedule
from fastapi import FastAPI

from src.core.pip.base_service import PipService
from src.core.scheduler.jobs.register_jobs import register_jobs


class Scheduler(PipService):
    def __init__(self, pip):
        super().__init__(pip)
        self.loop: AbstractEventLoop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.cease_continuous_run = threading.Event()
        self.schedule_thread = None
        self.loop_thread = None
        self.running = False

    def start(self):
        if not self.running:
            register_jobs(self.loop, self.pip)

            # Start the background thread
            self.run_continuously()

            # Start the asyncio event loop in a separate thread
            self.loop_thread = threading.Thread(target=self.loop.run_forever)
            self.loop_thread.start()

            self.running = True

    def run_continuously(self, interval=1):
        """Continuously run, while executing pending jobs at each
        elapsed time interval.
        @return cease_continuous_run: threading.Event which can
        be set to cease continuous run. Please note that it is
        *intended behavior that run_continuously() does not run
        missed jobs*. For example, if you've registered a job that
        should run every minute and you set a continuous run
        interval of one hour then your job won't be run 60 times
        at each interval but only once.
        """

        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not self.cease_continuous_run.is_set():
                    schedule.run_pending()
                    time.sleep(interval)

        self.schedule_thread = ScheduleThread()
        self.schedule_thread.start()
        return self.cease_continuous_run

    def init_app(self, app: FastAPI):
        @app.on_event("shutdown")
        def shutdown_event():
            print("Shutting down scheduler threads..")

            # Stop the schedule thread
            self.cease_continuous_run.set()

            # Stop the asyncio loop
            self.loop.call_soon_threadsafe(self.loop.stop)
            self.loop_thread.join()

            print("Scheduler threads shut down.")

    @staticmethod
    def signal_handler(signal, frame):
        sys.exit(0)

    def delayed(self, code, delay: int):
        """Run the provided code after a specified delay."""

        async def delayed_task():
            await asyncio.sleep(delay)
            code()

        asyncio.run_coroutine_threadsafe(delayed_task(), self.loop)
