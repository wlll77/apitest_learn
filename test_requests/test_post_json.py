import requests

# json_data ={
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
#   }
# r = requests.post("https://jsonplaceholder.typicode.com/posts",json = json_data)
# print(r.status_code)
# print(r.json())


"""
有道翻译
"""

r = requests.post("https://dict.youdao.com/keyword/key", data={"text": "Hello"})
print(r.status_code)
print(r.json())
