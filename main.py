from src import app_graph, State, APIRequest, APIResponse, GET_PRODUCTS, GET_ORDER_STATUS
from config import MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB
from sqlalchemy import create_engine, text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# uvicorn main:app --reload --port 8000

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    # Cho phép tất cả các phương thức (GET, POST, etc.)
    allow_headers=["*"],    # Cho phép tất cả các header
)

@app.post("/chat")
def read_root(request: APIRequest):
    data: State = {
        'user_input': request.user_input,
        'user_id': request.user_id,
    }
    result: State = app_graph.invoke(data)
    api_response = APIResponse(system_output=result['system_output'])
    return api_response


#Ket noi voi mysql
mysql_url = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
engine_mysql_debug = create_engine(mysql_url, echo=True, future=True)

@app.get("/products")
def get_products():
    query_text = GET_PRODUCTS
    try:
        with engine_mysql_debug.connect() as connection:
            result = connection.execute(text(query_text))
            rows = [dict(row._mapping) for row in result]
            print(f"Ket noi thanh cong, csdl tra ve danh sach sp\n {rows}")
    except Exception as e:
        print(f'Loi khi thuc thi truy van: {e}')
        return {"error": str(e)}

    # Trả về JSON
    return {"data": rows}

@app.get("/orderStatus/{user_id}")
def get_orderStatus(user_id: str):
    try:
        with engine_mysql_debug.connect() as connection:
            # Truyền tham số thay vì format
            result = connection.execute(text(GET_ORDER_STATUS), {"user_id": user_id})
            rows = [dict(row._mapping) for row in result]
            print(f"Ket noi thanh cong, csdl tra ve chi tiet don hang\n {rows}")
    except Exception as e:
        print(f'Loi khi thuc thi truy van: {e}')
        return {"error": str(e)}

    return {"data": rows}
