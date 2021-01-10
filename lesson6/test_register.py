from connect_mysql import

def delete_user():


def test_register(unlogin):
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": "test123456",
        "password": "123456",
        "mail":"123456@qq.com"
    }
    r = unlogin.post(url, body)
    print(r.text)