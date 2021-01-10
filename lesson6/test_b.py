import  pytest

@pytest.mark.parametrize("y",["abc","123","中文"])
@pytest.mark.parametrize("x",["abc","123","中文"])
def test_y(s, x, y):
    print("\n测试数据x: %s" % x )
    print("测试数据y: %s" % y )