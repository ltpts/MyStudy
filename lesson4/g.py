import requests
# 创建一个会话, 理解成一个无界面的浏览器
# 大小写Session是一样的
s  = requests.Session()
url = "http://49.235.92.12:7005/admin/login/"
r1 = s.get(url)
# 会话里面的cookie
print(s.cookies)
r2 = s.post(url)

# 自己添加cookie
cooks = {
    "yoyo":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
# 加到会话
s.cookies.update(cooks)
print(s.cookies)

s.post(url)

# 自己添加cookie
cooks2 = {
    "yoyo":"xxxxxxxxxxxxaaaaaaaaaaaaaa"
}
# 加到会话
s.cookies.update(cooks2)
print(s.cookies)

# 取出cookie
cooks3 = r1.cookies
print(cooks3)
print(dict(cooks3)['csrftoken'])
# s.get(url=url,cookies = r1.cookies)
s.get(url=url,cookies = dict(cooks3))
