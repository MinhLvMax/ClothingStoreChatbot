from typing import TypedDict, Optional, Literal
from .models import LLM


class State(TypedDict, total=False):
    user_input: str
    system_output: str
    model: LLM
    classify_chat_result: Optional[Literal["natural", "shopping"]]
    natural_response: str
    intent_classify_result: str
    is_login: bool
