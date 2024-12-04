s=input("Enter the string  : ")
flag=True
for i in s:
    if((i>='0' and i<='9') or (i>='A' and i<='Z') or (i>='a' and i<='z')):
        pass
    else:
        flag=False
        break

if(flag): print("The string contains only alphanumeric characters")
else : print("The string does not contain only alphanumeric cahracters")