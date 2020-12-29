import requests
import json

def login(s, usr="test", pwd="123456"):
    ''''登陆功能'''
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username":usr,
        "password":pwd
    }
    # r = requests.post(url, json=body)
    r = s.post(url, json=body)
    print(r.text)
    token = r.json().get('token')
    print(token)
    # token更新到头部
    h = {
        "Authorization":"Token %s"% token
    }
    s.headers.update(h)
    return r

if __name__ == '__main__':
    '''开发自测代码-测试函数功能'''
    s = requests.Session()
    login(s)
    url2 =  "http://49.235.92.12:7005/api/v1/userinfo"
    r2 = s.get(url2)
    print(r2.text)

