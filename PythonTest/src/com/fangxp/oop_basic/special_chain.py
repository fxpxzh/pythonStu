class Chain(object):

    def __init__(self, path='1'):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

#链式调用
c = Chain().status.user.timeline.list
print(c)

