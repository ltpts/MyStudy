import requests
import re #正则表达式
# session会话 保持cookies
s = requests.session() # requests 高级代码方式

url = "http://49.235.92.12:8020/admin/login/"
# 打开登录首页, 获取cookie
r = s.get(url)

# 正则 从 html 页面获取 csrftoken
csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
print(csrftoken)
# cookies
# print(s.cookies)

#  下次请求 post登录请求
body = {
    "csrfmiddlewaretoken": csrftoken[0],
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/"
}
r2 = s.post(url)
# print(s.cookies)

assert  "站点管理 | Django 站点管理员" in r2.text