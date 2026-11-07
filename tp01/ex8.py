# Exercice 8 - Opérations arithmétiques
x = int(input("x = "))
y = int(input("y = "))
print("Somme :", x + y)
print("Différence :", x - y)
print("Produit :", x * y)
if y != 0:
    print("Quotient :", x / y)
    print("Reste de la division entière :", x % y)
else:
    print("Division par zéro impossible (y = 0).")
