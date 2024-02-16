class StudentRating:
    def __init__(self, ratings=[]):
        self.ratings = ratings

    def set_ratings(self, ratings):
        self.ratings = ratings

    def add_rating(self, rating):
        self.ratings.append(rating)

    def count_excellent(self):
        return sum(1 for rating in self.ratings if 91 <= rating <= 100)

    def count_very_good(self):
        return sum(1 for rating in self.ratings if 71 <= rating <= 90)

    def count_good(self):
        return sum(1 for rating in self.ratings if 60 <= rating <= 70)

    def count_satisfactory(self):
        return sum(1 for rating in self.ratings if 0 <= rating <= 59)

    def __str__(self):
        rating_str = ""
        for rating in self.ratings:
            if 91 <= rating <= 100:
                rating_str += f"{rating}: excellent\n"
            elif 71 <= rating <= 90:
                rating_str += f"{rating}: very good\n"
            elif 60 <= rating <= 70:
                rating_str += f"{rating}: good\n"
            elif 0 <= rating <= 59:
                rating_str += f"{rating}: satisfactory\n"
        return rating_str


ratings = [85, 92, 45, 67, 78, 95, 55, 100, 41, 50, 91, 47, 63]
student_rating = StudentRating(ratings)

print("Кількість студентів з рейтингом 'excellent':", student_rating.count_excellent())
print("Кількість студентів з рейтингом 'very good':", student_rating.count_very_good())
print("Кількість студентів з рейтингом 'good':", student_rating.count_good())
print("Кількість студентів з рейтингом 'satisfactory':", student_rating.count_satisfactory())

print("Рейтинги студентів:")
print(student_rating)
