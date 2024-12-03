n=int(input("Enter the number : "))
num=n
s=0
while n>0 :
    s= s + (n%10)
    n=n//10
print("The given number is ",num," and the sum of the digits of the number is : ",s)