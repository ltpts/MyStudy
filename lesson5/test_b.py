
#
# def setup():
#     # 每条测试用例都会执行一次
#     print("\n前置操作:先登陆")
#
#
# def teardown():
#     print("\n后置操作:用例结束后,做一些数据清理")

# 前置的范围,让整个moudle只执行一次
def setup_module():
    print("\n前置操作,整个模块只执行一次")

def teardown_module():
    print("\n后置操作,整个模块只执行一次")

def test_1():
    print("测试1")

def test_2():
    print("测试2")

def test_3():
    print("测试3")

def test_4():
    print("测试4")