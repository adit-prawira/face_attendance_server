class ErrorMessage:
    def __init__(self, message:str, statusCode:int):
        self.message = message
        self.status = statusCode

    def getMessageBody(self):
        return {"message":self.message, "status":self.status}