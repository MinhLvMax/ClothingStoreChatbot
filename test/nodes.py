from src.graph import app_graph
from src.state import State

if __name__ == '__main__':
    # str = app_graph.get_graph().draw_ascii()
    # print(str)
    user_input = "Xin chào bạn, hãy cho thông tin về đơn hàng của tôi"
    data: State = {
        'user_input': user_input,
    }
    app_graph.invoke(data)
