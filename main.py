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


password_list = []

for m in range(0, nr_letters):
    password_list += random.choice(letters)
for n in range(0, nr_symbols):
    password_list += random.choice(symbols)
for o in range(0, nr_numbers):
    password_list += random.choice(numbers)

print(password_list)  #See the values added the list

random.shuffle(password_list) #shuffle the order of the list

print(password_list)        #See the new list

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")