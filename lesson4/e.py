import jsonpath

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
msg = jsonpath.jsonpath(data, '$.msg')
print(msg) # ['sucess!']
age = jsonpath.jsonpath(data, '$..age')
print(age)
mail = jsonpath.jsonpath(data, "$..mail")
print(mail)