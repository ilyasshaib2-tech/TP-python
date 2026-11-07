Nom1 = input("Taper nom 1 : ")
Age1 = int(input("Taper age 1 : "))

Nom2 = input("Taper nom 2 : ")
Age2 = int(input("Taper age 2 : "))

Nom3 = input("Taper nom 3 : ")
Age3 = int(input("Taper age 3 : "))

NomMax = Nom1
AgeMax = Age1

if Age2 > AgeMax:
    NomMax = Nom2
    AgeMax = Age2

if Age3 > AgeMax:
    NomMax = Nom3
    AgeMax = Age3

print("La personne la plus agee est :", NomMax)