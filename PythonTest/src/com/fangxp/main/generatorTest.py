'''
Created on Mar 11, 2016
 generator
@author: xianpanfang
'''
g = (x*x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))

# call generator manually:
s = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    l =[1]
    yield l
    while True:
        l = [1] +[l[i] + l[i+1] for i in range(len(l) - 1)] + [1]
        yield l

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break