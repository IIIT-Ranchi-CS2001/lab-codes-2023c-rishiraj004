import math
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=b*b-4*a*c
if(d==0):
    print("The only root of the equation is : ",-b/(2*a))
elif(d>0):
    print("The two roots of the equation are : ",(-b+math.sqrt(d))/(2*a)," and ",(-b-math.sqrt(d))/(2*a))
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("The equation has two complex roots: R1 = ",real ,"+", imaginary,"i", "R2 = ",real, "-", imaginary,"i")