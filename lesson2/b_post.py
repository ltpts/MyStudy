import requests

url = "http://49.235.92.12:7005/api/v4/login"

body = {
    "username": "test1",
    "password": "123456"
}

r = requests.post(url,data=body)
print(r.text)