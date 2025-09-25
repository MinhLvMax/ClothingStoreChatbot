from src import app_graph, State
from fastapi import FastAPI

app = FastAPI()
#uvicorn main:app --reload


@app.get("/{user_input}")
def read_root(user_input: str):
    data: State = {
        'user_input': user_input
    }
    result = app_graph.invoke(data)
    return result