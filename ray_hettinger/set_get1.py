class AwwYeah(object):
    def __init__(self):
        self._bar = 'Connie'

    @property
    def foo(self):
        return "More please: {}".format(self._bar)

    @foo.setter
    def foo(self, value):
        self._bar = '{} is great!'.format(value)

a = AwwYeah()
print(a.foo)
a.foo = "Chet"
print(a.foo)


