list1 = []
x = int(input("Enter the no. of course codes: "))
for i in range(x):
    y = input(f"Enter course code {i+1}: ")
    list1.append(y)
print(list1)

list2 = []
w = int(input("Enter the number of course names: "))
for i in range(w):
    z = input(f"Enter course name {i+1}: ")
    list2.append(z)
print(list2)

new_list = []
for i in range(min(len(list1), len(list2))):
    new_list.append(list1[i] + ":" + list2[i])
print(new_list)
