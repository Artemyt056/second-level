class MobPhone:
    def __init__(self, brand, size_h, size_w, price):
        self.brand = brand
        self._size_h = size_h
        self._size_w = size_w
        self._price = price

    def get_size_h(self):
        return self._size_h

    def set_size_h(self, value):
        if value > 0:
            self._size_h = value

    def get_size_w(self):
        return self._size_w

    def set_size_w(self, value):
        if value > 0:
            self._size_w = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value >= 0:
            self._price = value

    def getData(self):
        print(f"Brand: {self.brand}")
        print(f"Size (height x width): {self._size_h} x {self._size_w}")
        print(f"Price: ${self._price}")


phone1 = MobPhone("Samsung", 160, 75, 999)
phone2 = MobPhone("Apple", 158, 73, 1499)

print("Дані про телефон 1:")
phone1.getData()
print("Дані про телефон 2:")
phone2.getData()
