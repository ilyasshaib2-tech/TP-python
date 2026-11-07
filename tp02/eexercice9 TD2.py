C = input("Taper un caractere : ")

if "A" <= C <= "Z":
    print("Lettre majuscule")
elif "a" <= C <= "z":
    print("Lettre minuscule")
else:
    print("Autre caractere")