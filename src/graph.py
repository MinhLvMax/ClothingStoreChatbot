from langgraph.graph import StateGraph
from .state import State
from .nodes import init, chat_classify, natural_response, intent_classify, unclear, get_product, is_login, \
    get_order_status, recommend_product, combine_result, final
from .routers import chat_classify_router, intent_classify_router, is_login_router

# Builder
builder = StateGraph(State)

# Nodes
builder.add_node(init.__name__, init)
# builder.add_node(chat_classify.__name__, chat_classify)
# builder.add_conditional_edges(chat_classify.__name__, chat_classify_router)
# builder.add_node(natural_response.__name__, natural_response)
# builder.add_node(intent_classify.__name__, intent_classify)
# builder.add_conditional_edges(intent_classify.__name__, intent_classify_router)
# builder.add_node(unclear.__name__, unclear)
# builder.add_node(get_product.__name__, get_product)
# builder.add_node(is_login.__name__, is_login)
# builder.add_conditional_edges(is_login.__name__, is_login_router)
# builder.add_node(get_order_status.__name__, get_order_status)
# builder.add_node(recommend_product.__name__, recommend_product)
# builder.add_node(combine_result.__name__, combine_result)
builder.add_node(final.__name__, final)

# Edges
# builder.add_edge(init.__name__, chat_classify.__name__)
builder.add_edge(init.__name__, final.__name__)
# builder.add_edge(get_product.__name__, combine_result.__name__)
# builder.add_edge(get_order_status.__name__, combine_result.__name__)

# Start, End
builder.set_entry_point(init.__name__)
# builder.set_finish_point(chat_classify.__name__)
# builder.set_finish_point(natural_response.__name__)
# builder.set_finish_point(unclear.__name__)
# builder.set_finish_point(combine_result.__name__)
# builder.set_finish_point(recommend_product.__name__)
builder.set_finish_point(final.__name__)
app_graph = builder.compile()
