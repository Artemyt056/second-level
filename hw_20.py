class List:
    def __init__(self, items):
        self.items = items

    def remove_elements(self, elements_to_remove):
        self.items = [item for item in self.items if item not in elements_to_remove]


list_1 = List([1, 1, 2, 3, 1, 2, 3, 4])  # де видаляти
val = [1, 3]  # що видаляти

list_1.remove_elements(val)
print(list_1.items)  # [2, 2, 4] - відповідь після видалення
