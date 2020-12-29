import requests
import json
url = "http://49.235.92.12:7005/api/v1/login"

body = {
    "username":"test",
    "password":"123456"
}
# h = {"content-type":"application/json"}
# r = requests.post(url, data=json.dumps(body),headers = h)
# print(r.text)

r = requests.post(url, json=body)
print(r.text)
# a = json.loads(r.text)
# print(a)
# print(a['token'])

#.json() requests 内置json解析器
token = r.json()['token']
print(token)

url2 = "http://49.235.92.12:7005/api/v1/userinfo"
h = {
    "Authorization": "Token %s" % token
}

r2 = requests.get(url2, headers=h)
print(r2.text)

# 取出mail
mail = r2.json()['data'][0]['mail']
print(mail)
