import pytest
import requests

def login_y(s,usr="test", pwd="123456"):
    url = "http://49.235.92.12:7005/api/v1/login"
    data = {
        "username":usr,
        "password":pwd
    }
    r = s.post(url,json=data)
    print(r.text)
    token = r.json().get('token')
    cookie={
        "Authorization":"Token %s"% token
    }
    s.headers.update(cookie)
    return s

@pytest.fixture(scope="session", name="s")
def login():
    s = requests.Session()
    login_y(s)
    print("前置操作")
    #return s
    yield s
    print("后置操作")
    s.close()

test_data = ['user1','user2']
# request 是pytest内置fixture
@pytest.fixture(scope='session',
                params=test_data)
def user(request):
    return request.param

@pytest.fixture(scope='session')
def unlogin():
    s = requests.Session()
    yield s
    s.close()