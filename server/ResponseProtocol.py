from config import *
class ResponseProtocol(object):
    @staticmethod
    def response_login_result(result,nickname,username):
        return DELIMITER.join([RESPONSE_LOGIN_RESULT,result,nickname,username])

    @staticmethod
    def response_chat(nickname,messages):
        return DELIMITER.join([REQUEST_CHAT,nickname,messages])