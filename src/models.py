from .log import record_log
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
import os
from typing import Type
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