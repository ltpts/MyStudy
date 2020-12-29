import requests

url = "http://www.example.com/"
'''
    注释
'''

body = '''
<?xml version="1.0" encoding = "UTF-8"?>
<com>
<REQ name = "杨蓉蓉">
<USER_ID>yangrongrong</USER_ID>
<COMMODITY_ID>123456</COMMODITY_ID>
<SESSION_ID>absbnmlmasbnfmasbm1213</SESSION_ID>
</REQ>
</COM>
'''

r = requests.post(url,data=body.encode('utf-8'))