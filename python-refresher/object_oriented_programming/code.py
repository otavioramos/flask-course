class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student('Rolf', (90, 90, 93, 78, 90))
print(f"Student's name: {student.name}")
print(f"Student's average grade: {student.average_grade()}")

print('------------------------------------------------')

student2 = Student('Bob', (78, 90, 82, 78, 87))
print(f"Student's name: {student2.name}")
print(f"Student's average grade: {student2.average_grade()}")