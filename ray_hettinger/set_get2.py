class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = temperature


c = Celsius()
c.temperature = 100
print(c.to_fahrenheit())

