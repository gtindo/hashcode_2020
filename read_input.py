from classes import Book, Library


def read_input(filename):
    nb_books = 0
    nb_libraries = 0
    nb_days = 0
    libraries = {}
    books = {}

    with open(filename) as f:
        # Read first line
        line = f.readline().split(" ")
        nb_books = int(line[0])
        nb_libraries = int(line[1])
        nb_days = int(line[2])

        # Read second line and load books
        scores = f.readline().split(" ")
        for i, score in enumerate(scores):
            books[i] = Book(id=i, score=int(score))

        print(books)

        lines = f.read().split("\n")
        print(lines)
        i = 0
        n = len(lines)
        while i < n-1:
            line_1 = lines[i].split(" ")
            line_2 = lines[i+1].split(" ")

            signup_time = int(line_1[1])
            process_speed = int(line_1[2])
            books_ids = line_2
            l_books = []

            for id in books_ids:
                l_books.append(books[int(id)])

            id = len(libraries)
            libraries[id] = Library(l_books, id, signup_time, process_speed)
            i = i + 2

    return nb_books, nb_libraries, nb_days, books, libraries
