'''
Created on Mar 10, 2016

@author: xianpanfang
'''
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ']) #使用两层循环，可以生成全排列

import os
print([d for d in os.listdir('.')])
print([d for d in os.listdir('D:/DEVWorkspace')])
print([d for d in os.listdir('D:\\DEVWorkspace')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
print([k + '=' + v for k, v in d.items()])

for k, v in d.items():
    print(k, '=', v)  # print(k+ '='+ v)

L1 = ['Hello', 'World', 18, 'Apple', None]
L = ['Hello', 'World', 'IBM', 'Apple']
L2 = [ d.lower() for d in L ]
L3 = [ d.lower() for d in L1 if isinstance(d, str) == True]
print(L2)
print(L3)

