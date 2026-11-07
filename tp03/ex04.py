n=int(input("la valeur de n : "))
s=0
for i in range(1,n-1):
    if n%i==0 :
        s=s+i
if s == n:
    print("ce nombre est un nombre parfait")
else:
 print("ce nombre nest pas un nombre parfait")