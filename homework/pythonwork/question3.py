# # 定义一个函数，输入任意三个学生的姓名，然后写入到 D 盘根目录下的 test.txt 中
#
# def fwirte(f):
#     # 如果不存在test.txt就重新创建
#     return
#
#
# if __name__ == '__main__':
#     a = []
#     for i in range(3):
#         a.append(input("请输入人名\n"))
#     fwirte()

if __name__ == '__main__':
    res = True
    s1 = "abcde"
    s2 = "caebd"
    if len(s1) != len(s2):
        res = False
    if len(s1) == len(s2):
        for i in s1:
            if i not in s2:
                res = False
                break
    print(res)
    a = [1,3,4,6,7,8]
    a.index(1)