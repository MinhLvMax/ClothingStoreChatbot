from src import app_graph, State, APIRequest, APIResponse
from fastapi import FastAPI

app = FastAPI()
#uvicorn main:app --reload


@app.post("/chat}")
def read_root(request: APIRequest):
    data: State = {
        'user_input': request.user_input
    }
    result: State = app_graph.invoke(data)
    api_response = APIResponse(system_output=result['system_output'])
    return api_response