from .state import State
from .models import LLM, ChatClassify, IntentClassify, CHAT_CLASSIFY_TEMPLATE, INTENT_CLASSIFY_TEMPLATE, \
    ASK_TO_CONNECT_STAFF_TEMPLATE
from .log import record_log
from config import MODEL
from langchain_core.prompts import PromptTemplate


@record_log
def init(data: State):
    llm = LLM(model=MODEL)
    extra_data: State = {
        'model': llm,
        'system_output': 'Đây là câu trả lời mặc định'
    }
    return extra_data


@record_log
def chat_classify(data: State):
    llm = data['model']
    user_input = data['user_input']
    prompt = PromptTemplate.from_template(CHAT_CLASSIFY_TEMPLATE).format(
        user_input=user_input,
    )
    chat_classify: ChatClassify = llm.structuredOutputChat(prompt, ChatClassify)
    extra_data: State = {
        'classify_chat_result': chat_classify.classify_chat_result,
    }
    return extra_data


@record_log
def natural_response(data: State):
    user_input = data['user_input']
    llm = data['model']
    natural_response = llm.singleChat(user_input)
    extra_data: State = {
        'natural_response': natural_response
    }
    return extra_data


# def meet_staff(data: State):
#     extra_data: State = {}
#     return extra_data

@record_log
def intent_classify(data: State):
    llm = data['model']
    user_input = data['user_input']
    prompt = PromptTemplate.from_template(INTENT_CLASSIFY_TEMPLATE).format(
        user_input=user_input,
    )
    chat_classify: IntentClassify = llm.structuredOutputChat(prompt, IntentClassify)
    print(chat_classify)
    extra_data: State = {
        'intent_classify_result': chat_classify.intent_classify_result,
    }
    return extra_data


@record_log
def unclear(data: State):
    llm = data['model']
    system_output = llm.singleChat(ASK_TO_CONNECT_STAFF_TEMPLATE)
    extra_data: State = {
        'system_output': system_output,
    }
    return extra_data


@record_log
def get_product(data: State):
    "Viet logic tim kiem san pham trong kho hang phu hop voi yeu cau nguoi dung"
    extra_data: State = {

    }
    return extra_data


@record_log
def is_login(data: State):
    # Viet logic kiem tra dang nhap va gan gia tri cho bien is_login trong state, viet router cho is_login
    extra_data: State = {
        'is_login': False
    }
    return extra_data


@record_log
def get_order_status(data: State):
    extra_data: State = {

    }
    return extra_data


@record_log
def combine_result(data: State):
    extra_data: State = {

    }
    return extra_data


@record_log
def recommend_product(data: State):
    # Dua ra goi y mua san pham bat ki dua tren trang thai kho hang
    extra_data: State = {

    }
    return extra_data

# def final(data: State):
#     llm = data['model']
#     system_output = llm.singleChat(data['user_input'])
#     extra_data: State = {
#         'system_output': system_output
#     }
#     return extra_data
