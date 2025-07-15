# final exersice - movie
def user_input_movieName():
    movie_name_input = input("type in a movie name  ")
    return movie_name_input

def user_input_movieGrade(last_movie):
    movie_name_input = input("type in a movie name  ")
    return movie_name_input

def main():
    #this is the main func
    movie_list = []
    end_flag = 0

    while end_flag == 0:
        last_movie = user_input_movieName()
        user_input_movieGrade(last_movie)
        # movie_list.append(last_movie)

        # print(movie_list)
        if last_movie == "quit":
            end_flag += 1


if __name__ == '__main__':
    main()