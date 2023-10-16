# 用户名密码登录
# 拿到登录的token，获取用户信息
import requests

class TestUser():
    token_1 = ""
    username_1 = ""

    def test_login(self):
        username = 'laobai'
        password = '123456'
        # res = requests.post("/login", json={"username":username,"password":password})
        token = "token"
        assert token == "token"
        # return token,username
        TestUser.token_1 = token
        TestUser.username_1 = username

    def test_userinfo(self):
        # token, username = self.test_login()
        headers = {
            "token":TestUser.token_1
        }

        assert headers['token'] ==TestUser.token_1
        assert TestUser.username_1 == "laobai"