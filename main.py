student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total_height = 0

for y in range(0, len(student_heights)):
    total_height += student_heights[y]

print(total_height)

average_height = total_height / len(student_heights)

print(average_height)