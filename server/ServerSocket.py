from socket import socket, AF_INET, SOCK_STREAM
from config import SERVER_IP, SERVER_PORT
class ServerSockect(socket):
    def __init__(self):
        super(ServerSockect, self).__init__(AF_INET, SOCK_STREAM)
        self.bind((SERVER_IP, SERVER_PORT))
        self.listen(128)

