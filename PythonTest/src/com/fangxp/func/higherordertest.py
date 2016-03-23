'''
Created on Mar 11, 2016

@author: xianpanfang
'''

f = abs
print(f(-10))

#变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs)) 

#mapReduce
def f(x):
    return x * x
l = [1,2,3,4,5,6,7,8,9]
print(list(map(f,l)))
l2 = list(range(1,10))
print(list(map(f,l2)))

#str 函数
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
def fn(x, y):
    return x * 10 + y
print(reduce(fn,[1,2,3,4,5]))

l3 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper()+name[1:].lower() #切片
print(list(map(normalize,l3)))

def prod(L):
    return reduce(lambda x,y:x*y,L)
print(prod([3, 5, 7, 9]))

