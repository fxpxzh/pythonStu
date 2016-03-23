#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
数组

Created on Mar 9, 2016

@author: xianpanfang
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print('hello classmates:%s'%classmates)
print(classmates.count('Bob'))
print(classmates[1])
classmates.append('Jim')
print(classmates)
classmates.pop(1)
print(classmates)
print(list(range(0,100)))
print(tuple(range(0,100)))
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

l1 = [1]    
l2 = [1]
print(l1+l2)

print(list(range(0)))

print('list')
print('for fetch test')
print('for fetch test2')
print('for fetch and checkout test2 !')
