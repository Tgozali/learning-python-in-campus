# final exersice - movie
def user_input():
    movie_name_input = input("type in a movie name  ")
    return movie_name_input

def main():
    last_movie  = user_input()
    movie_list = []

    movie_list.append(last_movie)

if __name__ == '__main__':
    main()