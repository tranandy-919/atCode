#!/usr/env/python3
def main():
    list = []
    name = input("What is your name: ")
    list.append(name.title())

    age = int(input("What is your age: "))
    list.append(age)

    movie = input("What is your favorite movie: ")
    list.append(movie.title())
    
    inner = []
    genre = input("What's the genre: ")
    actor = input("Name one actor: ")
    inner.append(genre.title())
    inner.append(actor.title())

    list.append(inner)

    print(f"Hello {list[0]}, you're {list[1]} years old and your favorite movie is {list[2]}.")
    print(f"The movie's genre is {list[3][0]} and {list[3][1]} acts in it.")
main()
