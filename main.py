"""
Print numbers from 1 to 100.
If the number is divisible by 3 then print Fizz instead of the number
If the number is divisible by 5 then print Buzz instead of the number
If the number is divisible by both then print FizzBuzz
"""


for m in range(1, 101):
    if (m % 3 == 0) and (m % 5 == 0):
        print("FizzBuzz")
    elif(m % 3 == 0):
        print("Fizz")
    elif(m % 5 == 0):
        print("Buzz")
    else:
        print(m)