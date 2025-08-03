from pydantic import BaseModel, Field


class TimerRequest(BaseModel):
    seconds: int = Field(..., description="the number of seconds for the timer")


class TimerResponse(BaseModel):
    response: str
