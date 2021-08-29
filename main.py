"""
Calculate the sum of all numbers between 1 to 100.
create for loop to go through all numbers. Remember to end the range at 101
Use if statement: if number is % 2 == 0, then add to sum_total
"""

sum_total = 0

for m in range(1, 101):
    if m % 2 == 0:
        sum_total += m

print(sum_total)

sum_total = 0
for n in range(2 , 101, 2):
    sum_total += n

print(sum_total)