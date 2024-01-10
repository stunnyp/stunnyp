from model.user import User

class Twit:
    def __init__(self, body, author: User):
        self.body = body
        self.author = author
