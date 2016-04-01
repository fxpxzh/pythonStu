from pyclbr import Function
class Chain(object):
    
    def user(self,name):
        self._name = name 
    
    def __init__(self, path='users'):
        self._path = path

    def __getattr__(self, path):
        if isinstance(path, Function):
            return Chain('%s/%s'%(self._path,))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

#链式调用
c = Chain().status.user.timeline.list
print(c)

