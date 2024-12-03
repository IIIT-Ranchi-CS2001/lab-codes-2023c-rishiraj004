names = [f"Student{i}" for i in range(1, 11)] 
roll_nos = [i for i in range(1, 11)] 
marks = [75, 89, 92, 68, 85, 77, 90, 93, 80, 78]
students_details = list(zip(names, roll_nos, marks))
sorted_students = sorted(students_details, key=lambda x: x[2])

print(sorted_students)