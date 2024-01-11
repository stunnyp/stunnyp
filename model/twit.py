from model.user import User

class Twit:
    def __init__(self, id,  body, author: User):
        self.id = id
        self.body = body
        self.author = author
    def JSON(self):
        return {"id" : self.id, "body" : self.body, "author" : self.author}
