name=input("Enter the name of the student : ")
roll=int(input("Enter the roll number : "))
marks=int(input("Enter the number : "))

print("Name: ",name)
print("Roll Number: ",roll)
print("Marks: ",marks)
if(marks==100): g=10
elif(marks>=50 and marks<100): g=marks//10+1
else: g=0
print("Grade Point: ",g)
if(g==10): rem="OUTSTANDING"
if(g==9): rem="VERY GOOD"
if(g==8): rem="GOOD"
if(g==7): rem="AVERAGE"
if(g==6): rem="PASS"
if(g==0): rem="FAIL"
print("Remarks: ",rem)