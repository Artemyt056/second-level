class List:
    def __init__(self, items):
        self.items = items

    def remove_elements(self, elements_to_remove):
        for element in elements_to_remove:
            while element in self.items:
                self.items.remove(element)


list_1 = List([1, 1, 2, 3, 1, 2, 3, 4])  # де видаляти
val = [1, 3]  # що видаляти

list_1.remove_elements(val)
print(list_1.items)  # [2, 2, 4] - відповідь після видалення
