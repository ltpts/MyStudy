import requests
import pytest
import os
from MyStudy.lesson6.read_yaml import  get_yaml
'''
测试数据和代码分离
'''
data_path = os.path.dirname(os.path.realpath(__file__))
yaml_file = os.path.join(data_path,"test_data.yml")
print("读取到文件地址：%s" % yaml_file)
test_data = get_yaml(yaml_file)
#测试数据
# test_data = [[
#     {
#         "name": "test",
#         "sex": 'M',
#         "age": 20,
#         "mail": "123456789@qq.com"
#     }, {"message": "update some data!", "code": 0}], [
#     {
#         "name": "test",
#         "sex": 'F',
#         "age": 20,
#         "mail": "123456789@qq.com"
#     }, {"message": "update some data!", "code": 0}], [
#     {
#         "name": "test",
#         "sex": "",
#         "age": 20,
#         "mail": "123456789@qq.com"
#     }, {"message": "update some data!", "code": 0}],[
#     {
#         "name": "test",
#         "sex": 'b',
#         "age": 20,
#         "mail": "123456789@qq.com"
#     }, {"message": "参数类型错误", "code": 3333}]]


@pytest.mark.parametrize("data,expected",test_data)
def test_modify(s,data,expected):
    url = "http://49.235.92.12:7005/api/v1/userinfo"
    r = s.post(url,json=data)
    print(r.json())
    assert r.json()['code'] == expected['code']
    assert r.json()['message'] == expected['message']

@pytest.mark.notoken
@pytest.mark.parametrize("data,expected",test_data)
def test_modify(data,expected):
    url = "http://49.235.92.12:7005/api/v1/userinfo"
    r = requests.post(url,json=data)
    print(r.text)
    # print(r.json())
    # assert r.json()['code'] == expected['code']
    # assert r.json()['message'] == expected['message']