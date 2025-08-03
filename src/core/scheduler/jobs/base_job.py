import asyncio
from asyncio import AbstractEventLoop

import schedule
from loguru import logger


class BaseJob:
    name = "base_job"
    loop = None
    schedule = schedule.every(5).seconds
    scheduled_job = None
    scheduled_jobs = []

    def __init__(self, loop, pip):
        from src.core.pip.brain import PipsBrain

        self.loop: AbstractEventLoop = loop
        self.pip: PipsBrain = pip
        self.register()

    def register(self):
        self.scheduled_job = self.schedule.do(self.coroutine, loop=self.loop)

    def coroutine(self, loop):
        asyncio.run_coroutine_threadsafe(self.run_job_with_log(), loop=loop)

    def run_once(self):
        asyncio.run_coroutine_threadsafe(self.run_job_with_log(), loop=self.loop)
        return schedule.CancelJob

    async def job(self):
        logger.info("Job ran successfully")

    async def run_job_with_log(self):
        logger.info(f"Scheduled job: {self.name} starting..")
        try:
            await self.job()
            logger.info(f"Scheduled job: {self.name} finished.")
        except Exception as e:
            logger.error(f"Scheduled job: {self.name} failed.")
