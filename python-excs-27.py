class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Test
s = Student("Khalid")
s.add_grade(85)
s.add_grade(95)
print("Average grade:", s.average())
