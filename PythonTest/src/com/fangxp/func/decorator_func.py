#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call  %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2016-03-30')

print(now.__name__)

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@logger('debug')
def today():
    print('2016-03-30')
    
today()    
print(today.__name__)


def log_wrapper(func):
    def wrapper(*args,**kw):
        print('begin call %s ' %func.__name__)
        func(*args,**kw)
        print('end call %s '%func.__name__)
    return wrapper

@log_wrapper
def f(): 
    print('2016')

f()
        
