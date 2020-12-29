import re
import json
data = {
    "msg": "sucess!",
    "code": 0,
    "data": [{
            "id": 15,
            "name": "test",
            "sex": "",
            "age": 21,
            "mail": "283340479@qq.com",
            "create_time": "2020-12-17"
        }
    ]
}
result = json.dumps(data) #json字符串
# print(type(data))
# print(data)
# print(type(result))
# print(result)

c = re.findall('"mail": "(.+?)"', result)
print(c)
