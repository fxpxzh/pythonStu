# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2016
 循环测试
@author: xianpanfang
'''
names = ['Jim','Michael','Bob','Tracy']
for name in names :
    print(name)
sum1 = 0
numbers = list(range(101))
print(numbers)     
for num in numbers :
    sum1 = sum1 + num
print('sum1:%d---'%sum1)

for num2 in range(10) :
    print(num2)

'''
while
'''    
sum2 = 0 
n = 99
while n>0 :
    sum2 = sum2 +n
    n = n-2
print(sum2)   

print('new branch')