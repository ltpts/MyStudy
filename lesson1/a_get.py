import requests

url = "http://api.juheapi.com/japi/toh"
query_string= {
    "key": "57d46b7258fc47e14290c33537f23d36",
    "v": "1.0",
    "month":12,
    "day":13,

}
r = requests.get(url, params=query_string)
print(r.text) # str
# print(r.headers) #headers
# 键值对获取
# print((r.headers['Date']))
print(r.content) # byte 类型
print(r.content.decode("utf-8")) #返回的html有乱码的时候用到

# print(r.status_code) #状态码
print(r.url) #response的url

print(r.encoding) # utf-8

print(r.cookies) # <RequestsCookieJar[]>

print(r.ok) # True 状态码小于400的时候