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

# # 解法二 list自带sort函数, 参数 cmp, key, reverse
# if __name__ == '__main__':
#     a = [20, 10, 13, 17, 54, 35, 7, 23]
#     a.sort()
#     print(a)
#
# if __name__ == '__main__':
#     a = "hello"
#     b = "world"
#     a, b = b, a
#     print(a+b)

# # 水仙花数
# import math
# if __name__ == '__main__':
#     s = []
#     for i in range(152, 1000):
#         a = i % 10
#         b = int(i % 100 / 10)
#         c = int(i / 100)
#         x = math.pow(2,3)
#         if i == math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3):
#             s.append(i)
#     print(s)

# if __name__ == '__main__':
#
#     class ListNode:
#         def __init__(self, x):
#             self.val = x
#             self.next = None
#
#
#     l1 = ListNode(1)
#     l2 = ListNode(2)
#     l3 = ListNode(2)
#     l4 = ListNode(4)
#
#     l1.next = l2
#     l2.next = l3
#     l3.next = l4
#     l4 = {'val': 4, 'next': None}
#     l3 = {'val': 3, 'next': {'val':4, 'next': None}}
#
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         t = head
#         if head == None:
#             return head
#         while t.next:
#             if t.val == t.next.val:
#                 t.next = t.next.next
#             else:
#                 t = t.next
#         return head
#
#     print(l1.next.next.next == l4)


if __name__ == '__main__':
    n = 0o000010100101000001111010011101
    res = 0
    count = 32
    mask = 1
    while 0 < count:
        res << 1
        res += mask & n ## (mask & n)
        n >> 1
        count -= 1
    print(res)