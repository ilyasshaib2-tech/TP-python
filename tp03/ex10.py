x=input("ecrire un nombre: ")
s=0
for i in(x):
    p=1
    for c in range(1,int(i)+1):
        p=p*c
    s=s+p
if s==int(x):
    print(x,"est un nombre fort")
else:
    print(x,"nest pas un nombre fort")