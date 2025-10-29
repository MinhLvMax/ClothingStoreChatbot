from pydantic import BaseModel

class APIRequest(BaseModel):
    user_input: str

class APIResponse(BaseModel):
    system_output: str