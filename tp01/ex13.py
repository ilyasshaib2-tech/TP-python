# Exercice 13 - Calcul du prix à payer
quantite = int(input("Quantité achetée : "))
prix_unitaire = float(input("Prix unitaire : "))
prix_total = quantite * prix_unitaire
reduction = prix_total * 15 / 100
prix_final = prix_total - reduction
print("Prix total avant réduction :", prix_total)
print("Montant de la réduction (15 %) :", reduction)
print("Prix final à payer :", prix_final)
