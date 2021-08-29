"""
For loop to find the largest value in a string of numbers
Use a if statement to compare values. if the value in the list is higher, then its the bigger one
"""

student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_value = 0

for m in range(0, len(student_scores)):
    if highest_value < student_scores[m]:
        highest_value = student_scores[m]

print(f"The highest value is {highest_value}")