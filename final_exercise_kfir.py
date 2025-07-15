# final exersice - movie
def user_input_movieName():
    movie_name_input = input("type in a movie name  ")
    return movie_name_input


def user_input_movieGrade(last_movie_name: str) -> int:
    movie_grade_input = input(f"enter grade for {last_movie_name} movie between 1-10 ")
    # converts the input grade from str to int
    movie_grade_input = int(movie_grade_input)
    return movie_grade_input


def check_grade_valid(movie_grade_input: int) -> bool:
    if movie_grade_input in range(1, 11):
        print("valid input of grade")
        return True
    else:
        print("bad input, try again")
        return False


def main():
    # this is the main func
    movie_dict = {}

    while True:
        # get inputs from user
        last_movie_name: str = user_input_movieName()
        # check if the use wants to quit
        if last_movie_name.lower() == "quit":
            print("good bye!")
            break

        while True:
            try:
                last_movie_grade: int = user_input_movieGrade(last_movie_name)
                if check_grade_valid(last_movie_grade):
                    # check validity of input between 1-10
                    # add to dict
                    movie_dict[last_movie_name] = last_movie_grade
                    print(movie_dict)
                    break  # valid grade, break inner loop

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

            print("\nFinal movie list with grades:")
            for name, grade in movie_dict.items():
                print(f"{name}: {grade}")


if __name__ == '__main__':
    main()
