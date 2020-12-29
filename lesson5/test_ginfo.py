
def test_get_info(s):
    url2 = "http://49.235.92.12:7005/api/v1/userinfo"
    r2 = s.get(url2)
    print(r2.text)