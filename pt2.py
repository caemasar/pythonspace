#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 字典 dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
print(d)
d.pop('Bob')
print(d)

# set 集合
s = set([1, 2, 3])
print(s)
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# list-->sort
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

# 不可变的str
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

# 函数
# abs()取绝对值
print(abs(100))
print(abs(-20))
print(abs(12.34))

print(max(2, 3, 1, -5))
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(l))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
