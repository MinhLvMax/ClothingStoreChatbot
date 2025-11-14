from .state import State
from .nodes import natural_response, intent_classify, unclear, get_product, is_login, get_order_status, \
    recommend_product


def chat_classify_router(data: State):
    classify_chat_result = data['classify_chat_result']
    if classify_chat_result == 'natural':
        return natural_response.__name__
    if classify_chat_result == 'shopping':
        return intent_classify.__name__


def intent_classify_router(data: State):
    intent_classify_result = data['intent_classify_result']
    if intent_classify_result == 'product':
        return get_product.__name__
    if intent_classify_result == 'order':
        return is_login.__name__
    if intent_classify_result == 'unclear':
        return unclear.__name__


def is_login_router(data: State):
    is_login = data['is_login']
    if is_login:
        return get_order_status.__name__
    else:
        return recommend_product.__name__
