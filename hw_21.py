class Potion:
    def __init__(self, color, volume):
        """ Ініціалізатор класу Potion
        :param color: list
        :param volume: int
        """
        self.color = color
        self.volume = volume

    def mix(self, other_potion) -> list and int:
        """ Прийматимає інший Potion об'єкт та повертати змішаний Potion еліксир(тобто метод викликається одним з
    об'єктів класу Potion, приймає другий об'єкт Potion в якості параметра і повертає Новий об'єкт класу Potion який
    є поєднанням двох попередніх об'єктів Potion, і міститить дані про новий еліксир
    який утворився при поєднанні попередніх).
        :param other_potion:
        :return: list and int
        """
        new_color = [(self.color[i] * self.volume + other_potion.color[i] * other_potion.volume) // (
                self.volume + other_potion.volume) for i in range(3)]
        new_volume = self.volume + other_potion.volume
        return Potion(new_color, new_volume)


potio_piperis = Potion([255, 255, 255], 7)
potio_developing = Potion([51, 102, 51], 12)
new_potion = potio_piperis.mix(potio_developing)

print("new_potion.color:", new_potion.color)
print("new_potion.volume:", new_potion.volume)
