from read_input import read_input


def scan_books(input_file):
    nb_books, nb_libraries, nb_days, books, libraries = read_input(input_file)

    lib_scores = []
    for lib in libraries:
        score = libraries[lib].compute_score()
        print(score)
        lib_scores.append((libraries[lib].id, score))

    lib_scores.sort(key=lambda x: x[1])
    lib_scores.reverse()

    print(lib_scores)
    print(libraries[0].process_speed)


scan_books("inputs/a_example.txt")
