#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式

print(list(range(1, 11)))

'''
要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
'''
# 方法一是循环
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 方法二
print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
# 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])
# os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
