from langgraph.graph import StateGraph
from .state import State
from .nodes import init, final

builder = StateGraph(State)
builder.add_node(init.__name__, init)
builder.add_node(final.__name__, final)

builder.add_edge(init.__name__, final.__name__)

builder.set_entry_point(init.__name__)
builder.set_finish_point(final.__name__)

app_graph = builder.compile()