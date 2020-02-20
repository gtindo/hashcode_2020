from read_input import read_input


def scan_books(input_file, output_file):
    print("Step 1 : Read input file")
    nb_books, nb_libraries, nb_days, books, libraries = read_input(input_file)

    print("Step 2 : Compute librairies scores")
    lib_scores = []
    for lib in libraries:
        score = libraries[lib].compute_score()
        print(score)
        lib_scores.append((libraries[lib].id, score))

    print("Step 3 : sort scores")
    lib_scores.sort(key=lambda x: x[1])
    lib_scores.reverse()

    print("Step 4 : Compute number of libraries to scan")
    nb_libraries_to_scan = 0
    total_signup = 0
    for lib in lib_scores:
        library = libraries[lib[0]]
        total_signup = total_signup + library.signup_time

        if total_signup >= nb_days:
            break
        else:
            nb_libraries_to_scan = nb_libraries_to_scan + 1

    print("Step 5 : Write output file")
    with open(output_file, "a+") as f:
        f.write(str(nb_libraries_to_scan) + "\n")
        start_time = 0
        for lib in lib_scores:
            library = libraries[lib[0]]
            library.sort_library()

            start = library.compute_time_to_start(start_time)
            start_time = start

            end = library.compute_time_to_finish()

            if start + end <= nb_days:
                duration = end
            else:
                duration = nb_days - start

            n = len(library.books)
            nb_books = n - (library.process_speed * duration)
            if nb_books < 0:
                nb_books = n

            f.write("{} {}".format(library.id, nb_books)+"\n")

            i = 0
            line = ""
            while i < nb_books:
                line = line + str(library.books[i].id) + " "
                i = i + 1

            f.write(line + "\n")

scan_books("inputs/a_example.txt", "outputs/output_example.txt")
