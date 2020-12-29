import requests

#url参数带中文， urlencode编码
url = "http://japi.juhe.cn/qqvaluate/qq"
query_string = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"中文"
}
r = requests.get(url, params=query_string)
print(r.text) #获取响应的文本内容
print(type(r.text)) #type是获取数据类型的函数
r.json()
#r.json requests里面的json解析器，转字典
# print(r.json())
# print(type(r.json()))