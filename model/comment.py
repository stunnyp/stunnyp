from model.user import User
from model.twit import Twit

class Comment:
    def __init__(self, body: Twit, author: User):
        self.body = body
        self.author = author