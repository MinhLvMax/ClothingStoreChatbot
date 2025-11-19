from typing import TypedDict, Optional, Literal
from .models import LLM


class State(TypedDict, total=False):
    user_input: str
    user_id: str
    system_output: str
    model: LLM
    classify_chat_result: Optional[Literal["natural", "shopping"]]
    # natural_response: str
    intent_classify_result: str
    is_login: bool
    product_data_string: str
    order_status_data_string: str
