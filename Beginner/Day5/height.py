student_heights = [180, 124, 165, 173, 189, 169, 146]
count = 0
height = 0

for i in student_heights:
    count += 1
    height = height + i

print(round(height/count,2))
