import math

a = float(input("Taper a : "))
b = float(input("Taper b : "))
c = float(input("Taper c : "))

if a == 0:
    if b == 0:
        print("Pas de solution" if c != 0 else "Infinite de solutions")
    else:
        print("Solution :", -c / b)
else:
    D = b * b - 4 * a * c
    print("Discriminant =", D)
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("Deux solutions :", x1, "et", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("Une solution double :", x)
    else:
        print("Pas de solution reelle")