class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Library:
    def __init__(self, books, id, signup_time, process_speed):
        self.id = id
        self.books = books
        self.signup_time = signup_time
        self.process_speed = process_speed

    def compute_time_to_start(self, last_library_signup_end):
        return last_library_signup_end + self.signup_time

    def sort_library(self):
        self.books.sort(key=lambda x: x.score)
        self.books.reverse()

    def compute_score(self):
        score = 0
        for book in self.books:
            score = score + book.score

        return score - self.signup_time + self.process_speed

    def compute_time_to_finish(self):
        n = len(self.books)
        return int(n / self.process_speed) + 1 + self.signup_time

