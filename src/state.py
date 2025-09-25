from typing import TypedDict
from .models import LLM

class State(TypedDict, total=False):
    user_input: str
    user_output: str
    model: LLM

