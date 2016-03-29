'''
Created on Mar 22, 2016

@author: xianpanfang
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88),('adb',99)]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)

def by_name(t):
    return t[0].lower()  #str.lower(t[0])
L3 = sorted(L,key=by_name,reverse = True)
print(L3)

print('hello')