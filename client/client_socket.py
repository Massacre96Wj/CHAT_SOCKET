from socket import socket, AF_INET,SOCK_STREAM
from config import SERVER_IP, SERVER_PORT
class ClientSocket(socket):
    def __init__(self):
        super(ClientSocket, self).__init__(AF_INET, SOCK_STREAM)

    def connect_server(self):
        self.connect((SERVER_IP, SERVER_PORT))

        self.setblocking(0)#非阻塞模式

    def recv_data(self):
        return self.recv(512).decode("utf-8")

    def send_data(self,messages):
        self.send(messages.encode("utf-8"))
