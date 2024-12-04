names = [f"Student{i}" for i in range(1, 11)] 
roll_nos = [i for i in range(1, 11)] 
marks = [75, 89, 92, 68, 85, 77, 90, 93, 80, 78]
students_details_manual = [(names[i], roll_nos[i], marks[i]) for i in range(len(names))]
for i in range(len(students_details_manual)):
    for j in range(0, len(students_details_manual) - i - 1):
        if students_details_manual[j][2] > students_details_manual[j + 1][2]:
            # Swap the elements
            students_details_manual[j], students_details_manual[j + 1] = students_details_manual[j + 1], students_details_manual[j]

print(students_details_manual)