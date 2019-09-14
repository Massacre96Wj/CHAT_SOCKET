from tkinter.messagebox import showinfo
from threading import Thread
from time import sleep
import sys
from request_protocol import  RequestProtocol
from window_login import  WindowLogin
from window_chat import  WindowChat
from client_socket import  ClientSocket
from config import *

class Client(object):
    def __init__(self):
        self.window = WindowLogin()
        self.room = WindowChat()
        self.room.withdraw()
        self.conn = ClientSocket()
        self.response_handle_functions = dict()
        self.is_running = True
        self.username = None
        self.register(RESPONSE_LOGIN_RESULT,lambda data:self.resonse_login_handle(data))
        self.register(RESPONSE_CHAT, lambda data:self.reponse_chat_handle(data))

    def startup(self):
        self.conn.connect_server()
        Thread(target=lambda:self.response_handle()).start()
        self.window.mainloop()

    def response_handle(self):
        while self.is_running:
            response_text = None
            try:
                response_text = self.conn.recv_data()
                print("response_text = {}".format(response_text))
            except BlockingIOError:
                sleep(0.1)
                continue
            response_data = self.parsing_response_text(response_text)
            handle_function = self.response_handle_functions[response_data["response_id"]]
            if handle_function:
                handle_function(response_data)

    @staticmethod
    def parsing_response_text(response_text):
        response_text_list = response_text.split(DELIMITER)
        response_data = dict()
        response_data["response_id"] = response_text_list[0]

        if response_text_list[0] == RESPONSE_LOGIN_RESULT:
            response_data["result"] = response_text_list[1]
            response_data["nickname"] = response_text_list[2]
            response_data["username"] = response_text_list[3]
        if response_text_list[0] == RESPONSE_CHAT:
            response_data["nickname"] = response_text_list[1]
            response_data["messages"] = response_text_list[2]
        return response_data

    def register(self, response_id, handle_function):
        self.response_handle_functions[response_id] = handle_function

    def response_login_handle(self, response_data):
        result = response_data["result"]
        print("result = {}".format(result))
        nickname = response_data["nickname"]
        if result == "0":
            showinfo("提示", "用户名或者密码错误")
            return
        self.username = response_data["username"]
        showinfo(("提示", "登陆成功"))

        #显示聊天窗口
        self.room.set_title(nickname)
        self.room.update()
        self.room.deiconify()

        #隐藏登录窗口
        self.window.withdraw()

    def response_chat_handle(self, response_data):
        nickname = response_data["nickname"]
        messages = response_data["messages"]

        self.room.append_message(nickname, messages)

        self.window.on_reset_button_click(lambda: self.clear_inputs())
        self.window.on_login_button_click(lambda: self.send_login_data())
        self.window.on_window_closed(lambda: exit())

        self.room.on_send_button_click(lambda: self.send_chat_data())
        self.room.on_window_closed(lambda: self.exit())

    def exit(self):
        self.is_running = False
        self.conn.close()
        sys.exit(0)

    def clear_inputs(self):
        self.window.clear_username()
        self.window.clear_password()

    def send_login_data(self):
        username = self.window.get_username()
        password = self.window.get_password()
        request_text = RequestProtocol.request_login(username,password)
        print('发送的聊天内容：', request_text)
        self.conn.send_data(request_text)

    def send_chat_data(self):
        chat_contents = self.room.get_input()
        self.room.clear_input()
        self.room.append_message("我", chat_contents)
        request_text = RequestProtocol.request_chat(self.username, chat_contents)
        self.conn.send_data(request_text)

if __name__ == '__main__':
     client = Client()
     client.startup()
