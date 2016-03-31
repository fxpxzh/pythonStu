#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__=('name','age') # 用tuple定义允许绑定的属性名称
    
class GraduateStudent(Student):
    pass

s = Student()
s.name = 'fangxp'
s.age = 18

try:
    s.score = 60
except AttributeError as e:
    print('AttributeError:', e)

#父类限定的属性 对继承的子类是不起作用的
g = GraduateStudent()
g.score = 79
print('g.score =', g.score)