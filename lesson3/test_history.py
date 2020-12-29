import requests

def test_today():
    '''key有效'''
    url = "http://api.juheapi.com/japi/toh"

    query_string = {
        "key": "57d46b7258fc47e14290c33537f23d36",
        "v": "1.0",
        "month": 11,
        "day": 1
    }
    r = requests.get(url, params=query_string)
    print(r.text)
    error_code = r.json()["error_code"]
    print(error_code)
    reason = r.json()['reason']
    print(reason)
    result = r.json()['result']
    print(result)
    print(type(result))

    assert error_code == 0
    assert reason == "请求成功！"
    assert len(result) >= 1
    # assert type(result) == list
    assert type(result) is list