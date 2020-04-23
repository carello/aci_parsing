"""
https://www.freecodecamp.org/news/python-property-decorator/
"""
class House(object):
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        print("boo")
        del self._price


house = House(222.34)
print(house.price)
house.price = 150.01
print(house.price)
del house.price



