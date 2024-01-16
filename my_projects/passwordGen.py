#!/usr/bin/env python3
import random
import string

# Functions
def special_prompt():
    punc = input("Would you like to include special characters? enter y for yes, any other input for no: ")
    return punc == "y"

def num_chars_prompt():
    while True:
        char_number = input("How many characters do you want for your password? ")
        if char_number.isdigit():
            char_number = int(char_number)
            return char_number
        else:
            char_number = input("How many characters do you want for your password? ")

def create_password(chars, char_number):
    # Looping to add random characters to a list until input number is met
    i = 0
    password = []
    while i < char_number:
        password.append(random.choice(chars))
        i += 1
        # once number of characters is met, turn list into a string and print to console
        if i == char_number:
            return ''.join(password)

def main():
    # Setting chars as upper and lowercase letters and punctuation characters
    special_or_not = special_prompt()
    if special_or_not == True:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits

    # request input for number of random characters
    char_number = num_chars_prompt()

    # create password
    print(create_password(chars, char_number))

def loop():
    run_again = 'y'
    while run_again == 'y':
        main()
        run_again = input('Would you like another password? enter y for yes, any other input for no: ')
    else:
        print("Goodbye!")

print("\n***** Password Generator *****\n")
print("The password generator creates passwords with letters and numbers by default.")
loop()
