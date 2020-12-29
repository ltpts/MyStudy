# 2. 求任意字符串的长度
# 解法一
# if __name__ == '__main__':
#     a = input("请输入任意字符串\n")
#     s = 0
#     for i in a:
#         s += 1
#     print("%s的长度是：%d" % (a, s))

# 解法二
if __name__ == '__main__':
    a = input("请输入任意字符串\n")
    print("%s 的长度是 %d" % (a, len(a)))