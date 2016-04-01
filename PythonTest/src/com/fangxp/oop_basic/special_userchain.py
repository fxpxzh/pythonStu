class Chain(object):
    
    def user(self,name):
        return Chain('%s/%s' % (self._path, name))
    
    def __init__(self, path='users'):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

#链式调用
c = Chain().user("Michael").repos
print(c)

