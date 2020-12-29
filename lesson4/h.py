import requests
import json
s = requests.session()
url = "http://49.235.92.12:7005/api/v1/login"

body = {
    "username":"test",
    "password":"123456"
}
r = s.post(url, json=body)

# token = r.json()["token"]
# print(token)
print(s.headers)
url2 = "http://49.235.92.12:7005/api/v1/userinfo"

h = {
    "Authorization":"token %s" % r.json()["token"]
}
# r2 = requests.get(url2, headers = h)

s.headers.update(h)
print(s.headers)
# 下个请求需要token
r2 = s.get(url2)
print(r2.text)

# token 令牌是识别身份的
