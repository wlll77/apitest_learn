import requests

# 创建一个会话
req = requests.Session()
url = 'http://sellshop.5istudy.online/sell/user/login'
data = {
    'username': 'test01',
    'password': '123456'
}
# 登录，req保存了cookie或者session
res = req.post(url, data=data)
# print(res.text)
url2 = 'http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10'
res1 = req.get(url2)
print(res1.text)


# 另一种方法，直接在headers里加cookie
# url = 'http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10'
# headers = {
#     'Cookie':'token=7a70fecd-fc4b-4152-92da-2f2160bfe077'
# }
#
# res = requests.get(url, headers=headers)
# print(res.text)
