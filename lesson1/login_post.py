import requests
import json

url = "http://49.235.92.12:7005/api/v1/login"

body = {
    "username":"test",
    "password":"123456"
}
# # content-type:application/json
# r = requests.post(url, json=body)
# print(r.text)

r = requests.post(url, data=j)