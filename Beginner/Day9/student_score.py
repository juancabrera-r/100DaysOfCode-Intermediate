student_db = {"Harry": 85, "Ron": 75, "Hermione": 95, "Draco": 75, "Neville": 50}

for key in student_db:
    score = student_db[key]
    if score >= 91:
        student_db[key] = "Outstanding"
    elif score >= 81:
        student_db[key] = "Exceeds expectations"
    elif score >= 71:
        student_db[key] = "Acceptable"
    else:
        student_db[key] = "Fail"

print(student_db)
