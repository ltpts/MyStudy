a = [1,2,3] # list
b = (1,2,3) # tuple

# array数组



print(type(a))
print(type(b))
print(b[0])

k = {
    "a" : None,
    "c" : "aaa",
    "d" : [1,2,3],
    "b" : {
        "a":111
    }
}

k['f'] = "abc"
print(k)

del k['b']
print(k)

# 集合
a = {1,2,3,4,'a','b','c', 57, "z", "v"}
b = {0,2,3,4,"a",'b', "h0", "m", 10}
print(set([9,12,10,10,2,2,5,5,7,9,0,12,5]))
c = a & b # a 交 b
print(c)
c = a | b # a 并 b
print(c)
c = b - a
print(c)