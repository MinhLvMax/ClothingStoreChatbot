from .log import record_log
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field
import os
from typing import Type, Literal
from dotenv import load_dotenv

load_dotenv()


class LLM:
    def __init__(self, model: str, api_key: str = os.getenv('GOOGLE_API_KEY')):
        self._model = ChatGoogleGenerativeAI(
            model=model,
            api_key=api_key,
        )

    @record_log
    def singleChat(self, user_input: str) -> str:
        return self._model.invoke(user_input).content

    @record_log
    def hisChat(self, history: list[BaseMessage]) -> str:
        result = self._model.invoke(history).content
        return result

    @record_log
    def structuredOutputChat(self, user_input: str, schema: Type[BaseModel]):
        runnable_object = self._model.with_structured_output(schema)
        class_output = runnable_object.invoke(user_input)
        return class_output


class ChatClassify(BaseModel):
    classify_chat_result: Literal["natural", "shopping"] = Field(
        description='''
        Phân loại hội thoại: natural (tự nhiên), shopping (mua hàng)
        Lưu ý: nếu đầu vào của người dùng liên quan đến sản phẩm, hay đơn hàng thì hãy phân loại là shopping
        '''
    )


class IntentClassify(BaseModel):
    intent_classify_result: Literal["product", "order", "unclear"] = Field(
        description="Phân loại ý định mua hàng: product (liên quan đến việc hỏi về sản phẩm), order (liên quan đến đơn hàng của người dùng), unclear (Chưa rõ ý định của người dùng)"
    )


CHAT_CLASSIFY_TEMPLATE = '''
    Hãy phân loại chat này dựa trên đầu vào của người dùng:
    "{user_input}"
'''

INTENT_CLASSIFY_TEMPLATE = '''
    Hãy phân loại loại ý định này dựa trên ý định mua hàng của người dùng:
    "{user_input}"
'''

ASK_TO_CONNECT_STAFF_TEMPLATE = '''
Hãy hỏi người dùng có muốn gặp nhân viên không?
'''
