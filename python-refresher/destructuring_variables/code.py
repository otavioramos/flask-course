t = 5, 11

# destructuring
x, y = t

print(x, y)

print('--------------------')
# ----------------------

student_attendance = {
    'Rolf': 96, 
    'Bob': 80, 
    'Anne': 100
}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')

print('--------------------')
# ----------------------
people = [
    ('Bob', 42, 'Mechanic'),
    ('James', 24, 'Artist'),
    ('Harry', 32, 'Lecturer')
]

for name, age, profession in people:
    print(f'Name: {name}, Age: {age}, Profession: {profession}')

print('--------------------')
# ----------------------

person = ('Bob', 42, 'Mechanic')

# by convention "_" in a variable name means that we don't expect to use that variable
name, _, profession = person

print(name, profession)

print('--------------------')
# ----------------------

head, *tail = [1, 2, 3, 4, 5]
print(f'Head: {head}')
print(f'Tail: {tail}')

print('--------------------')
# ----------------------

*head, tail = [1, 2, 3, 4, 5]
print(f'Head: {head}')
print(f'Tail: {tail}')