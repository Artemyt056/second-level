class MobPhone:
    def __init__(self, brand: str, size_h: float, size_w: float, price: float):
        """Ініціалізатор класу MobPhone.
        :param brand: Бренд мобільного телефону.
        :param size_h: Висота мобільного телефону.
        :param size_w: Ширина мобільного телефону.
        :param price: Ціна мобільного телефону.
        """
        self._brand = brand
        self._size_h = self._validate_size(size_h)
        self._size_w = self._validate_size(size_w)
        self._price = self._validate_price(price)

    def _validate_size(self, size: float) -> float:
        """Метод для перевірки та обмеження введеного розміру.
        :param size:  Розмір, тобто висота та ширина телефону
        :return: Очищений та обмежений розмір.
        """
        if size <= 0:
            return 0
        elif size > 10:
            return 10
        else:
            return size

    def _validate_price(self, price: float) -> float:
        """ Метод для перевірки та обмеження введеної ціни.
        :param price: ціна телефону
        :return: очищенна та обмежена ціна
        """
        if price < 0:
            return 0
        else:
            return price

    def get_brand(self):
        """ Геттер для отримання бренду мобільного телефону
        """
        return self._brand

    def get_size_h(self):
        """Геттер для отримання висоти мобільного телефону."""
        return self._size_h

    def get_size_w(self):
        """Геттер для отримання ширини мобільного телефону."""
        return self._size_w

    def get_price(self):
        """Геттер для отримання ціни мобільного телефону."""
        return self._price

    def set_size_h(self, size_h):
        """Сеттер для встановлення висоти мобільного телефону."""
        self._size_h = self._validate_size(size_h)

    def set_size_w(self, size_w):
        """Сеттер для встановлення ширини мобільного телефону."""
        self._size_w = self._validate_size(size_w)

    def set_price(self, price):
        """Сеттер для встановлення ціни мобільного телефону."""
        self._price = self._validate_price(price)

    def getData(self) -> str:
        """Метод для отримання даних про мобільний телефон."""
        return f"Бренд: {self._brand}, Розмір (висота x ширина): {self._size_h} x {self._size_w}, Ціна: {self._price}"


phone1 = MobPhone("Samsung", 6.5, 3.0, 1000)
phone2 = MobPhone("Apple", 6.1, 2.98, 1500)

print("Дані про мобільний телефон 1:")
print(phone1.getData())

print("Дані про мобільний телефон 2:")
print(phone2.getData())

phone1.set_size_h(7.0)
phone1.set_size_w(3.5)
print("Оновлені дані про мобільний телефон 1 після зміни розміру:")
print(phone1.getData())
