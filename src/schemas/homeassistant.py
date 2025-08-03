from pydantic import BaseModel, Field


class CommandRequest(BaseModel):
    prompt: str = Field(
        ..., description="the smart home prompt, simplified as much as possible."
    )


class CommandResponse(BaseModel):
    response: str
