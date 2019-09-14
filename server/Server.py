from threading import Thread
from ServerSocket import ServerSockect
from SocketWrapper import SocketWrapper
from ResponseProtocol import ResponseProtocol
from DB import DB
from config import *
class Server(object):
    def __init__(self):
        self.server_socket = ServerSockect()
        self.clients = dict()
        self.request_handle_functions = dict()
        self.register(REQUEST_LOGIN, lambda sf, data:self.request.login_handle(sf, data))
        self.register(REQUEST_CHAT, lambda sf, data: self.request.login_handle(sf, data))

    def startup(self):
        while 1:
            sock, addr = self.server_socket.accept()
            print("sock = {},addr = {}".format(sock, addr))
            client_sock = SocketWrapper(sock)
            print("开启进程")
            Thread(target=lambda :self.request_handle(client_sock)).start()

    def request_handle(self, client_sock):
        while 1:
            request_text = client_sock.recv_data()
            print("request_text = {}".format(request_text))
            if not request_text:
                print("客户端下线")
                self.remove_offline_user(client_sock)
                break
            print("接收到的数据{0}".format(request_text))
            request_data = self.parse_request_text(request_text)
            handle_function = self.request_handle_function(request_data['request_id'])
            if handle_function:
                handle_function(client_sock,request_data)

    def remove_offline_user(self,client_sock):
        username = None
        for uname, csock in self.clients.items():
            if csock['sock'].sock == client_sock.sock:
                username = uname
        del self.clients[username]

    @staticmethod
    def parse_request_text(request_text):
        request_text_list = request_text.split(DELIMITER)
        request_data = dict()
        request_data['request_id'] = request_text_list[0]
        if request_text_list[0] == REQUEST_LOGIN:
            request_data['username'] = request_text_list[1]
            request_data['password'] = request_text_list[2]
        if request_text_list[0] == REQUEST_CHAT:
            request_data['username'] = request_text_list[1]
            request_data['messages'] = request_text_list[2]
        return  request_data

    def register(self, request_id, handle_function):
        self.request_handle_functions[request_id] = handle_function

    def request_login_handle(self, client_sock, request_data):
        username = request_data['username']
        password = request_data['password']

        ret,nickname,username = self.check_user_login(username,password)
        if ret == '1':
            self.clients[username] = {'sock':client_sock, 'nickname':nickname}
        response_text = ResponseProtocol.response_login_result(ret, nickname, username)
        client_sock.send_data(response_text)

    def check_user_login(self, username, password):
        sql = "select * from users where username = '" + username + " '"
        db_conn = DB()
        results = db_conn.get_one(sql)
        if not results or results['user_password'] != password:
            return "0", "", username
        return "1", results["user_nickname"], username

    def request_chat_handle(self, client_sock, request_data):
        username = request_data['username']
        messages = request_data['messages']
        nickname = client_sock[username]['nickname']
        response_text = ResponseProtocol.response_chat(nickname, messages)
        for uname, csock in self.clients.items():
            if  uname == username:
                continue
            csock['sock'].send_data(response_text)
if __name__ == '__main__':
    server = Server()
    server.startup()
