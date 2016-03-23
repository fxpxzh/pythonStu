'''
Created on Mar 10, 2016

@author: xianpanfang
'''

help(abs)
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
print(n1,n2)
print('n1:%d,n2:%d'%(n1,n2))

'''
 define fuc
'''
from myabstest import my_abs
print(my_abs(-5)) 

'''
 定义list tuple参数函数
'''
def calc(numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n*n
    return sum1
#调用时需要传入list、tuple
print(calc([1,2,3]))

'''
定义可变参数   函数参数前添加*
同理 传入参数是也可以传list或tuple在前加*
'''
def calc1(*numbers):
    sum2 = 0 
    for n in numbers:
        sum2 = sum2 + n*n
    return sum2
print(calc1(1,2,3))
nums = [2,3,5]
print(calc1(nums[0],nums[1],nums[2]))
print(calc1(*nums))

