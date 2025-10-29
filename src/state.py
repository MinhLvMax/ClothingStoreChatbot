from typing import TypedDict
from .models import LLM


class State(TypedDict, total=False):
    user_input: str
    system_output: str
    model: LLM
