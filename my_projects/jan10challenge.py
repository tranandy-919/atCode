#!/usr/env/python3
def main():
    list = []
    name = input("What is your name: ")
    name = name.title()
    list.append(name)

    age = input("What is your age: ")
    int(age)
    list.append(age)

    movie = input("What is your favorite movie: ")
    movie = movie.title()
    list.append(movie)
    
    inner = []
    genre = input("What's the genre: ")
    actor = input("Name one actor: ")
    inner.append(genre.title())
    inner.append(actor.title())

    list.append(inner)

    print(f"Hello {list[0]}, you're {list[1]} years old and your favorite movie is {list[2]}.")
    print(f"The movie's genre is {list[3][0]} and {list[3][1]} acts in it.")
main()
