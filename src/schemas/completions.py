from pydantic import BaseModel


class CompletionsRequest(BaseModel):
    prompt: str


class CompletionsResponse(BaseModel):
    response: str
