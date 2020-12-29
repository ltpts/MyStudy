import requests

url = "http://api.juheapi.com/japi/toh"
query_string= {
    "key": "57d46b7258fc47e14290c33537f23d36",
    "v": "1.0",
    "month":12,
    "day":13,

}
body ={
    "key1":"2222",
    "key2":"1111"
}
headers={
    "token":"1111111111",
    "version":"1.1"
}
cookie={
    "k111":"2222222",
    "c2":"fddddd123"
}
r = requests.post(url,
                  params=query_string,
                  json=body,
                  headers=headers,
                  cookies=cookie)
print(r.text) # str