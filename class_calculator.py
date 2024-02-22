class Calculator:
    @staticmethod
    def add(x, y) -> int or float:
        """Додавання двох чисел"""
        return x + y

    @staticmethod
    def subtract(x, y) -> int or float:
        """Віднімання одного числа від іншого"""
        return x - y

    @staticmethod
    def multiply(x, y) -> int or float:
        """Множення двох чисел"""
        return x * y

    @staticmethod
    def divide(x, y) -> int or float:
        """Ділення першого числа на друге"""
        if y == 0:
            raise ValueError("Ділення на нуль неможливе")
        return x / y

    @staticmethod
    def power(x, y) -> int or float:
        """Піднесення першого числа до степеня другого"""
        return x ** y

    @staticmethod
    def square_root(x) -> int or float:
        """Квадратний корінь числа"""
        if x < 0:
            raise ValueError("Корінь з від'ємного числа неможливий")
        return x ** 0.5
