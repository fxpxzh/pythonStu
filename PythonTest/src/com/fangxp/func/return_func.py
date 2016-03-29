#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

#fix count()
def count2():
    fs = []
    def f(n):
        def j():
            return n*n
        return j
    for i in range(1,4):
        fs.append(f(i))
    return fs   

f1, f2, f3 = count2()


#fix count()
def count5():
    fs = []
    def f():
        return lambda x:x*x
    for i in range(1,4):
        fs.append(f()(i))
    return fs   

f1, f2, f3 = count5()

print('count5 f1:%s'%f1)
print('count5 f2:%s'%f2)
print('count5 f3:%s'%f3)

#fix count()
def count6():
    fs = []
    def f():
        g =  lambda x:x*x
        return g
    for i in range(1,4):
        fs.append(f()(i))
    return fs   

f1, f2, f3 = count5()

print('count5 f1:%s'%f1)
print('count5 f2:%s'%f2)
print('count5 f3:%s'%f3)

g = lambda n : n*n
print(g(4))

def e(n):
    return lambda x : n*x 
g = e(2)
print(g(2))
#lambda fix
def count3():
    fs = []
    def f(n):
        return lambda x : n*x 
    for i in range(1,4):
        g = f(i)
        fs.append(g(i))
    return fs
 
f1, f2, f3 = count3()
 
print(f1)
print(f2)
print(f3)

def count4():
    fs = []
    for i in range(1,4):
        g = lambda x : x*x
        fs.append(g(i))
    return fs
    
f1, f2, f3 = count4()
print(f1)
print(f2)
print(f3)