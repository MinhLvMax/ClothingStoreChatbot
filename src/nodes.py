from .state import State
from .models import LLM
from .log import record_log
from config import MODEL

def init(data: State):
    llm = LLM(model=MODEL)
    extra_data: State = {
        'model' : llm,
    }
    return extra_data

def final(data: State):
    llm = data['model']
    user_output = llm.singleChat(data['user_input'])
    extra_data: State = {
        'user_output': user_output
    }
    return extra_data
