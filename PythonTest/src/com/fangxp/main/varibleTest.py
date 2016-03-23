#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Mar 9, 2016

@author: xianpanfang
'''

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'  #r''表示''内部的字符串默认不转义
s4 = r'"Hello,Lisa!"'
print(n);
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print('\\\t\\')   #转义
'''  
测试多行注释
'''
s5=r'"niaho"'
print(s5)
print(r'''ni
hao1''')
print('''ni
hao2''')
print('''ni
'hao3''')
print('中文测试')
print(format(15877631.23,'.2e')) #科学计数法
print(format(0.0015,'.2e')) #科学计数法
print(float(1))
print(int(1.1))
