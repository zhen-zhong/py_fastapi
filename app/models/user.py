# app/models/user.py (模拟的 SQLAlchemy 模型)

class User:
    def __init__(self, id, username, email, hashed_password, is_active=True):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active