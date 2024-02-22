from datetime import datetime


class Train:
    def __init__(self, destination: str, train_number: int, departure_time: datetime):
        """Ініціалізатор класу Train.

        :param destination: Пункт призначення потягу.
        :param train_number: Номер потягу.
        :param departure_time: Час відправлення потягу.
        """
        self._destination = destination
        self._train_number = train_number
        self._departure_time = departure_time

    @property
    def destination(self) -> str:
        """Повертає пункт призначення потягу
        :return: пункт призначення потягу
        """
        return self._destination

    @property
    def train_number(self) -> int:
        """Повертає номер потягу
        :return: номер потягу
        """
        return self._train_number

    @property
    def departure_time(self) -> datetime:
        """ Повертає час відправлення потягу
        :return: час відправлення потягу
        """
        return self._departure_time

    @staticmethod
    def sort_trains_by_number(train_list: list) -> list:
        """Сортує список потягів за номерами.
        :param train_list: Список об'єктів класу Train.
        :return: Відсортований список потягів за номерами.
        """
        return sorted(train_list, key=lambda train: train.train_number)

    @staticmethod
    def get_train_info_by_number(train_list: list, number: int) -> list:
        """Повертає інформацію про потяги з заданим номером
        :param train_list: Список об'єктів класу Train
        :param number: Номер потягу
        :return: Список об'єктів класу Train, які мають вказаний номер.
        """
        return [train for train in train_list if train.train_number == number]

    @staticmethod
    def sort_trains_by_destination_and_time(train_list: list) -> list:
        """Сортує список потягів за пунктом призначення та часом відправлення
        :param train_list: Список об'єктів класу Train.
        :return: Відсортований список потягів за пунктом призначення та часом відправлення.
        """
        return sorted(train_list, key=lambda train: (train.destination, train.departure_time))


train1 = Train("Kyiv", 101, datetime(2024, 2, 15, 8, 0))
train2 = Train("Lviv", 102, datetime(2024, 2, 15, 10, 0))
train3 = Train("Kyiv", 103, datetime(2024, 2, 15, 9, 0))
train4 = Train("Odessa", 104, datetime(2024, 2, 15, 9, 30))
train5 = Train("Kyiv", 105, datetime(2024, 2, 15, 10, 30))

trains = [train1, train2, train3, train4, train5]

sorted_trains = Train.sort_trains_by_number(trains)
print("Сортування за номерами потягів:")
for train in sorted_trains:
    print(train.train_number, train.destination, train.departure_time)

train_info = Train.get_train_info_by_number(trains, 103)
print("Інформація про потяг з номером 103:")
for train in train_info:
    print(train.train_number, train.destination, train.departure_time)

sorted_trains_advanced = Train.sort_trains_by_destination_and_time(trains)
print("Сортування за пунктом призначення та часом відправлення:")
for train in sorted_trains_advanced:
    print(train.train_number, train.destination, train.departure_time)
