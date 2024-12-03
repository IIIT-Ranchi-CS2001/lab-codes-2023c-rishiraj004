s=input("Enter the sentence : ")
l=s.split()
count=0
for words in l:
    if(words == words[::-1]):
        count+=1

print("There are ",count," palindrome words in the sentence")