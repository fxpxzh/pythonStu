#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())

#不要把实例属性和类属性使用相同的名字，
#因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)
print(Student.name)

