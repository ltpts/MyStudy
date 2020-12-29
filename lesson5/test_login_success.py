import requests
from lesson5.login_function import login
import json


def test_login_success():
    '''正常账号,正常密码'''
    s = requests.Session()
    res = login(s)
    code = res.json()["code"]
    assert code == 0

def test_login_fail():
    '''错误账号'''
    s = requests.Session()
    res = login(s,'test_fail')
    code = res.json()["code"]
    assert code == 3003