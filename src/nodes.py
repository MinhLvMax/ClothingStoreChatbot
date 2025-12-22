from .state import State
from .models import LLM, ChatClassify, IntentClassify, CHAT_CLASSIFY_TEMPLATE, INTENT_CLASSIFY_TEMPLATE, \
    ASK_TO_CONNECT_STAFF_TEMPLATE, PRODUCT_CONSULTING_TEMPLATE, ORDER_STATUS_PROMPT_TEMPLATE, NATURAL_RESPONSE_TEMPLATE, SYSTEM_MESSAGE
from .log import record_log
from config import MODEL, PRODUCTS_endpoint, ORDER_STATUS_endpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
import requests
import json



@record_log
def init(data: State):
    llm = LLM(model=MODEL)

    response = requests.get(PRODUCTS_endpoint)
    json_product = response.json()
    products_str = json.dumps(json_product, ensure_ascii=False, indent=2)
    sys_mes_str = PromptTemplate.from_template(SYSTEM_MESSAGE).format(
        products=products_str
    )
    print(sys_mes_str)
    user_input = data['user_input']
    print(user_input)
    his = [SystemMessage(content=sys_mes_str), HumanMessage(content=user_input)]
    sys_out = llm.hisChat(his)

    extra_data: State = {
        # 'model': llm,
        'system_output': sys_out,
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
    prompt = PromptTemplate.from_template(NATURAL_RESPONSE_TEMPLATE).format(
        user_input=user_input,
    )
    natural_response = llm.singleChat(prompt)
    # natural_response = "Xin lỗi, chúng tôi chỉ hỗ trợ trả lời các thông tin liên quan đến mua hàng. Bạn có câu hỏi nào khác không?"
    extra_data: State = {
        'system_output': natural_response
    }
    return extra_data

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
    llm = data['model']
    user_input = data['user_input']
    endpoint_product = PRODUCTS_endpoint
    try:
        response = requests.get(endpoint_product)
        data = response.json()
        products_str = json.dumps(data, ensure_ascii=False, indent=2)
        prompt = PromptTemplate.from_template(PRODUCT_CONSULTING_TEMPLATE).format(
            user_input=user_input,
            products = products_str
        )
        mess = llm.singleChat(prompt)
    except Exception as e:
        products_str = "Không tìm thấy sản phẩm"
        mess = f"Có lỗi khi gọi API lấy sản phẩm:\n {e}"

    extra_data: State = {
        'system_output': mess,
        'product_data_string': products_str
    }
    return extra_data


@record_log
def is_login(data: State):
    # Viet logic kiem tra dang nhap va gan gia tri cho bien is_login trong state, viet router cho is_login
    user_id = data.get('user_id', None)
    is_login = False
    if user_id:
        is_login = True
    extra_data: State = {
        'is_login': is_login,
    }
    return extra_data


@record_log
def get_order_status(data: State):
    llm = data['model']
    user_input = data['user_input']
    user_id = data['user_id']
    try:
        response = requests.get(ORDER_STATUS_endpoint, params={'user_id': user_id})
        data = response.json()
        oder_status_str = json.dumps(data, ensure_ascii=False, indent=2)
        prompt = PromptTemplate.from_template(ORDER_STATUS_PROMPT_TEMPLATE).format(
            user_input=user_input,
            order_status = oder_status_str
        )
        mess = llm.singleChat(prompt)
    except Exception as e:
        oder_status_str = "Người dùng chưa đặt đơn hàng nào"
        mess = f"Có lỗi khi gọi API lấy api sản phẩm:\n {e}"
    extra_data: State = {
        'system_output' : mess,
        'order_status_data_string': oder_status_str,
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

def final(data: State):
    # llm = data['model']
    # system_output = llm.singleChat(data['user_input'])
    extra_data: State = {

    }
    return extra_data
