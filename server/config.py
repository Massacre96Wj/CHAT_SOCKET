'''
Server.py:服务器端程序类，负责服务器端的运行流程
ServerSocket.py:服务器套接字类，常见服务器套接字
SockectWrapper.py：套接字包装类，用于包装客户端套接字，指定传输编码格式
ResponseProtocal.py:响应拼接类，按照协议规定的格式凭借服务器端的响应
DB.py数据库类
'''

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8090

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = '415563'
DB_PORT = 3306
DB_NAME = 'min_chat'

REQUEST_LOGIN = '00001'
REQUEST_CHAT = '00002'
RESPONSE_LOGIN_RESULT = '1001'
RESPONSE_CHAT = '1002'
DELIMITER = '|'