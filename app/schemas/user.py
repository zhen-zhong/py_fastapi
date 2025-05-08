from pydantic import BaseModel


# 用户登录模型
class UserLogin(BaseModel):
    username: str
    password: str


# 用户注册模型
class UserRegister(BaseModel):
    username: str
    password: str
    email: str


# 忘记密码模型
class ForgotPassword(BaseModel):
    email: str
