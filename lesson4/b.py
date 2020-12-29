import json
# dict
k = {
    "a" : None,
    "e" : True,
    "f" : False,
    "c" : "BaN",
    "d" : ['1',2,3],
    "g" : ('a',2,3),
    "b" : {
        "a":111,
        'b':True
    }
}

# json 实际上是字符串
# dump 对文件进行转换
dict_to_json = json.dumps(k)
print(k)
print(type(k))
print(dict_to_json)
print(type(dict_to_json))


# json 数据转dict
json_to_dict = json.loads(dict_to_json)
print(json_to_dict)