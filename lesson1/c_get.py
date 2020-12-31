import requests
import urllib3
urllib3.disable_warnings() # 忽略ssl相关的警告
# InsecureRequestWarning
url = "https://www.cnblogs.com/yoyoketang/"

# SSL: CERTIFICATE_VERIFY_FAILED
r=requests.get(url,verify=False)
print(r.text)
# print(r.json()) # JSONDecodeError
#test操作
