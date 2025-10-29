from .state import State
from .models import LLM
from config import MODEL

def init(data: State):
    llm = LLM(model=MODEL)
    extra_data: State = {
        'model' : llm,
    }
    return extra_data

def final(data: State):
    llm = data['model']
    system_output = llm.singleChat(data['user_input'])
    extra_data: State = {
        'system_output': system_output
    }
    return extra_data
