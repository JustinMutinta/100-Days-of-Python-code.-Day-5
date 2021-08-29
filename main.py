"""
Password generator.
Ask user for number of letters in the password
Ask user for number of symbols in password
Ask user for number of numbers in password
Generate random password with above parameters
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
Create variable to hold letters/numbers/symbols
Use for loop to go from range 0 to 'users choice'
add value to new variable
"""

letters_var = ""
symbols_var = ""
numbers_var = ""

for m in range(0, nr_letters):
    letters_var += letters[random.randint(0, len(letters) - 1)]
for n in range(0, nr_symbols):
    symbols_var += symbols[random.randint(0, len(symbols) - 1)]
for o in range(0, nr_numbers):
    numbers_var += numbers[random.randint(0, len(numbers) - 1)]

print(letters_var + symbols_var + numbers_var)
