x=input("Enter a word: ")
c= ""
for i in (x):
     c= f"{i}{c}"
if c==x:
     print("palindrome")
else:
        print("not palindrome")