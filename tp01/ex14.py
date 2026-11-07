# Exercice 14 - Conversion de monnaie (MAD -> EUR)
mad = float(input("Montant en dirhams (MAD) : "))
taux = float(input("Taux de conversion MAD -> EUR : "))
euros = mad * taux
print(mad, "MAD =", euros, "EUR")
