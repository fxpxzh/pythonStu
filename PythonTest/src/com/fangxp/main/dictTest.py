'''
Created on Mar 10, 2016
 dict 测试 set
@author: xianpanfang
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Thomas' in d)#in判断是否存在
print(d.get('Thomas'))
print(d.get('Thomas', -1))
s1 = set([1, 2, 3])
print(s1)
l1 = [1,2,3]
s2 = set(l1)
# s3=set([2,l1,5])     #错误 set中key不可变 不能为list
print(s2)
a = 'abc'
b = a.replace('a', 'b')
print('a:%5s'%a +'nihao')
print('b:%5s'%b)
t1 = (1,2,3)
t2 = (1,[2,3])
print(t1)
print(t2)

print('test22222! for conflict merge test!')

print('branch commit test!')
