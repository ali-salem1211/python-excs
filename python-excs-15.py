def student_grades():
    students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 90
    }

    total = sum(students.values())
    average = total / len(students)

    print("Class Average:", average)

student_grades()
