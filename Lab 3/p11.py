n=int(input("Enter the number of terms : "))
if(n>=1) : print(0,end="")
if(n>=2) : print(", ",1,end="")
a=0;b=1;c=0;i=2
while i<=n:
    c=a+b
    a=b
    b=c
    print(", ",c,end="")
    i = i+1