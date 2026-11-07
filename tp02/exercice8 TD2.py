Max = int(input("Taper nombre 1 : "))

for i in range(3):
    N = int(input("Taper nombre suivant : "))
    if N > Max:
        Max = N

print("Le plus grand est :", Max)