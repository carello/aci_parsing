class Person:
    def __init__(self, name):
        self.name = name

bob = Person('Bob Smith')
print(bob.name)
print("------------------")


class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def foo(self):
        "name property docs"
        print('fetch...')
        return self._name

bob2 = Person2('Bob2 Smith')
print(bob2.foo)

print("---------")

class Person3:
    def __init__(self, name):
        self.name = name

    @property
    def _foo(self):
        "name property docs"
        print('fetch...')
        return self.name

bob3 = Person3('Bob3 Smith')
print(bob3._foo)


print("---------")
print("---AT 4 ------")

class Person4:
    def __init__(self, name):
        self.name = name

    @property
    def foo(self):
        "name property docs"
        print('fetch...')
        return self.name

    @foo.setter
    def foo(self, value):
        "name property docs"
        print('fetch...')
        self.name = value

bob4 = Person4('Bob4 Smith')
print(bob4.name)
bob4.name = "chet"
print(bob4.foo)


print("---------")
print("---AT 5 ------")

class Person5:
    def __init__(self, name):
        self.name = name

    def to_fahrenheit(self):
        return self.name + "Connie"

    @property
    def foo(self):
        "name property docs"
        print('fetch...')
        return self.name

    @foo.setter
    def foo(self, value):
        "name property docs"
        print('fetch...')
        self.name = value

bob5 = Person5('Bob5 Smith5')
print(bob5.name)
bob5.name = "chet5"
print(bob5.foo)
result = bob5.to_fahrenheit()
print(result)


print("---------")
print("---AT 6 ------")

class Person6:
    def __init__(self, name):
        self._name = name

    def combo_name(self):
        return self.name + "Connie"

    @property
    def name(self):
        "name property docs"
        print('fetch getter...')
        return self._name

    @name.setter
    def name(self, value):
        "name property docs"
        print('fetch setter...')
        self._name = value

bob6 = Person6('Bob6 Smith6')
print(bob6.name)
bob6.name = "chet6"
print(bob6.name)
result = bob6.combo_name()
print(result)

