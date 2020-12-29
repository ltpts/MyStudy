# a = range(1,10) # [1,2,3,4,5,]
# print(a)
# print(type(a))
# print(list(a))
# a = range(1, 10, 3)
# print(list(a))
#
# def funcx(x):
#     return x*x
#
# a = funcx((4))
#
# print(a)
# f = lambda x: x*x
# a = f(2)
# print(a)



# 面试题: *args, **kwargs是什么意思

def info(agr1,*agr2):
    print("输出:%s" % agr1)
    print(agr2)

# info(1,2,3,4,5,6,[1,2,3,45,6])
# # 输出:1
# # (2, 3, 4, 5, 6, [1, 2, 3, 45, 6])
#
# c = [1,2,3,4,5,6]
# info(3, *c)
# # 输出:3
# # (1, 2, 3, 4, 5, 6)

def infos(arg1,**kwargs):
    print("输出:%s" % arg1)
    print(kwargs)
    print(kwargs['a'])

infos(3,a=1,b=2,c=3,d=4)
# 输出:3
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
infos(4, **d)


def funcxx(*args, **kwargs):
    print(args)
    print(kwargs)

funcxx(1,2,3,4,5,6,a=1,b=2,c=3)