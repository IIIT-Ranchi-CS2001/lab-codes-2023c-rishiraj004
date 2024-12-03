s=input("Enter the string : ")
c=input("Enter the character you want to count : ")
count=0
for i in s:
    if(i==c): count+=1
print(c," appears ",count," times in ",s)
