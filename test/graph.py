from src import app_graph
from src import State

def test_graph():
    data: State = {
        'user_input': "Xin chào"
    }
    result = app_graph.invoke(data)
    print(result)

if __name__ == '__main__':
    test_graph()
    pass