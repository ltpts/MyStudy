# 输入任意三个整数，将它们从小到大排列并输出
# 解法1
# def MySort(*args):
#     '''冒泡排序'''
#     for i in range(len(a)):
#         for j in range(len(a) - 1 - i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1],a[j]
#     return a
# if __name__ == '__main__':
#     a = []
#     print("请输入三个整数,enter键作为间隔")
#     for i in range(3):
#         a.append(int(input()))
#     print(MySort(a))
#

# 解法二 list自带sort函数, 参数 cmp, key, reverse
if __name__ == '__main__':
    a = [20, 10, 13, 17, 54, 35, 7, 23]
    a.sort()
    print(a)