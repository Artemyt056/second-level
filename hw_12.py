class StudentRating:
    def __init__(self, ratings: list):
        """ Ініціалізує клас StudentRating.
        :param ratings: empty list with ratings
        """
        self._ratings = ratings

    def set_ratings(self, ratings: list):
        """Встановлює список рейтингів студентів."""
        self._ratings = ratings

    def add_rating(self, rating: int):
        """Додає новий рейтинг до списку."""
        self._ratings.append(rating)

    def get_maximum_rating(self) -> int:
        """Повертає максимальний рейтинг в групі.
        :return: maximum_rating
        """
        if not self._ratings:
            return None
        return max(self._ratings)

    def get_minimum_rating(self) -> int:
        """Повертає мінімальний рейтинг в групі.
        :return: minimum_rating
        """
        if not self._ratings:
            return None
        return min(self._ratings)

    def get_average_rating(self) -> int:
        """Повертає середній рейтинг групи.
        :return: average_rating
        """
        if not self._ratings:
            return None
        return sum(self._ratings) / len(self._ratings)

    def get_higher_than_average_count(self) -> int:
        """Повертає кількість студентів з рейтингом вищим за середній.
        :return: higher_than_average_rating_count
        """
        if not self._ratings:
            return 0
        average = self.get_average_rating()
        return sum(1 for rating in self._ratings if rating > average)

    def get_lower_than_average_count(self) -> int:
        """Повертає кількість студентів з рейтингом нижчим за середній
        :return: lower_than_average_rating_count
        """
        if not self._ratings:
            return 0
        average = self.get_average_rating()
        return sum(1 for rating in self._ratings if rating < average)

    def get_excellent_count(self) -> int:
        """Повертає кількість студентів з рейтингом excellent
        :return: excellent_rating_count
        """
        return sum(1 for rating in self._ratings if rating >= 91)

    def get_very_good_count(self) -> int:
        """Повертає кількість студентів з рейтингом very good
        :return: very_good_rating_count
        """
        return sum(1 for rating in self._ratings if 71 <= rating <= 90)

    def get_good_count(self) -> int:
        """ Повертає кількість студентів з рейтингом good
        :return: good_rating_count
        """
        return sum(1 for rating in self._ratings if 60 <= rating <= 70)

    def get_satisfactory_count(self) -> int:
        """Повертає кількість студентів з рейтингом satisfactory
        :return: satisfactory_rating_count
        """
        return sum(1 for rating in self._ratings if 0 <= rating <= 59)

    def to_string(self) -> str:
        """Повертає рядок, що містить усі рейтинги у вигляді рядка.
        :return: str of all ratings
        """
        return ', '.join(map(str, self._ratings))


ratings = [50, 75, 90, 40, 65, 100, 91, 23, 57, 82, 97, 10, 31, 47, 59, 64, 76, 89]
sr = StudentRating(ratings)
print("Максимальний рейтинг:", sr.get_maximum_rating())
print("Мінімальний рейтинг:", sr.get_minimum_rating())
print("Середній рейтинг:", sr.get_average_rating())
print("Кількість студентів з рейтингом вище за середній:", sr.get_higher_than_average_count())
print("Кількість студентів з рейтингом нижче за середній:", sr.get_lower_than_average_count())
print("Кількість студентів з рейтингом 'excellent':", sr.get_excellent_count())
print("Кількість студентів з рейтингом 'very good':", sr.get_very_good_count())
print("Кількість студентів з рейтингом 'good':", sr.get_good_count())
print("Кількість студентів з рейтингом 'satisfactory':", sr.get_satisfactory_count())
print("Всі рейтинги:", sr.to_string())

