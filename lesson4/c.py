import json

d = {"a":True, "b":123}
f = '{"a":True, "b":123}'

print(d)
print(f)

# eval() 把字符串当代码去执行
print(eval(f))

# g = json.loads(f) # JSONDecodeError