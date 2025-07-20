# final exercise - movie tracker
import os
import json


def movieDict_json_export(movie_dict):
    with open("movies.json", "w") as f:
        json.dump(movie_dict, f)


def movieDict_json_import():
    if os.path.exists("movies.json"):
        with open("movies.json", "r") as f:
            return json.load(f)
    return {}


def user_input_movieName():
    movie_name_input = input("type in a movie name  ")
    return movie_name_input


def user_input_movieGrade(last_movie_name: str) -> int:
    movie_grade_input = input(f"enter grade for {last_movie_name} movie between 1-10 ")
    # converts the input grade from str to int
    movie_grade_input = int(movie_grade_input)
    return movie_grade_input


def average_grade(movie_dict: dict) -> float:
    sum_of_grades = sum(movie_dict.values())
    return (sum_of_grades / len(movie_dict))


def highest_grade_moviename(movie_dict: dict) -> str:
    max_grade = max(movie_dict.values())
    favorite_movie_name = [key for key, value in movie_dict.items() if value == max_grade]
    print(favorite_movie_name)  # ['Barbie']
    return favorite_movie_name


def check_grade_valid(movie_grade_input: int) -> bool:
    if movie_grade_input in range(1, 11):
        print("valid input of grade")
        return True
    else:
        print("bad input, try again")
        return False


def main():
    # this is the main func
    movie_dict = movieDict_json_import()

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
                    # save it - use dump
                    movieDict_json_export(movie_dict)
                    print(movie_dict)
                    # calculate average
                    print(f" the average grade is {average_grade(movie_dict)} out of 10")
                    # print highest grade
                    print(
                        f" the {highest_grade_moviename(movie_dict)} got the highest grade - {max(movie_dict.values())} out of 10")

                    break  # valid grade, break inner loop

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

    print("\nFinal movie list with grades:")
    for name, grade in movie_dict.items():
        print(f"{name}: {grade}")


if __name__ == '__main__':
    main()
