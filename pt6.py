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
