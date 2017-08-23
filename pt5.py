#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
'''
切片
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
#前10个数，每两个取一个：
print(L[:10:2])
#所有数，每5个取一个
print(L[::5])
#什么都不写，只写[:]就可以原样复制一个list
print(L[:])
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[::2])


'''
迭代

JAVA:
for (i=0; i<list.length; i++) {
    n = list[i];
}
'''
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
    print(d[key])
for value in d.values():
    print(value)
for k, v in d.items():
    print(k,',',v)

for ch in 'ABC':
    print(ch)
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

'''
判断是否可以迭代
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
'''
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)