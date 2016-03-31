#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

print(int('12345', base=8))

print(int('1000000',base=2))

def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

