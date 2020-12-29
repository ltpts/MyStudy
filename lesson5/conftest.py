import sys, os
import pytest
from MyStudy.lesson5.login_function import login
import requests

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

@pytest.fixture(scope="session",name="s")
def login_s():
    s = requests.Session()
    login(s)
    # return s
    yield s
    print("后置操作")