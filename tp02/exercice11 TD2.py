J = int(input("Taper un nombre entre 0 et 6 : "))

if J == 0:
    print("Dimanche")
elif J == 1:
    print("Lundi")
elif J == 2:
    print("Mardi")
elif J == 3:
    print("Mercredi")
elif J == 4:
    print("Jeudi")
elif J == 5:
    print("Vendredi")
elif J == 6:
    print("Samedi")
else:
    print("Erreur : nombre hors intervalle")