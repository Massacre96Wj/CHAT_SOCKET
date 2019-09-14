class SocketWrapper(object):
    def __init__(self,sock):
        self.sock = sock
    def recv_data(self):
        return self.sock.recv(512).decode("utf-8")
    def send_data(self,messages):
        return self.sock.send(messages.encode("utf-8"))