#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print ('中文测试正常')

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

s1 = 72
s2 = 85
r = (s2-s1)/s2*100

#这个地方要注意的是，输出"%"需要写"%%"
print('%.1f%%' % r)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

t = ('a', 'b', ['A', 'B'])
#下面这句是错误的t作为一个tuple是不可变的是read-only，对应里面的list是不能变大小的
#t[2].append = 'X'
t[2][0] = "x"

print(t)


classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[-1])
print(classmates[-2])
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = 'Sarah'
print(classmates)


L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(len(s))

#好像不支持直接限定变量类型，只能附不同类型的值
#age = int(input("input your age:"))
age = 23
print('your age is ',end='')
print(age)
if age >= 18:
    print('adult')
else:
    print('teenager')

height = 1.75
weight = 70.5

bmi = weight/(height*height)
print(bmi)
if bmi>32:
    print('严重肥胖')
elif bmi>28:
    print('肥胖')
elif bmi>25:
    print('过重')
elif bmi>18.5:
    print('正常')
elif bmi<28:
    print('过轻')