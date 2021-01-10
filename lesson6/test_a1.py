import pytest
import requests


# 测试数据用list of tuple, list of list
@pytest.mark.parametrize("test_input, expected", [("1+1", 2), ("2-1", 1), ("1*3", 1), ("6/2", 3)])
def test_x(test_input, expected):
    print("\n test_input, expected : %s %s" % (test_input, expected))
    assert eval(test_input) == expected
    assert eval("1+1") == 2

@pytest.fixture()
def login_fixture():
    print("前置操作")

@pytest.mark.parametrize("test_input, expected",
                         [({"username":123456,"password":123456}, 1),
                          ({"username":123456,"password":""}, 0),
                          ({"username":"","password":123456}, 0)])
def test_y(login_fixture, test_input, expected):
    print("\n 测试账号：%s，测试密码：%s \n 期望结果: %d" % (test_input["username"], test_input["password"], expected))
    # assert eval(test_input) == expected
    # assert eval("1+1") == 2
