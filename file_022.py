while True:
    try:
        # Demander la saisie d'un nombre
        nombre = int(input("Entrez un nombre entier non négatif : "))

        # Vérifier si le nombre est positif ou nul
        if nombre >= 0:
            break
        else:
            print("Erreur: Le nombre doit être non négatif. Réessayez.")
    except ValueError:
        print("Erreur: Vous devez entrer un nombre entier. Réessayez.")

# Calcul de la factorielle
factorial = 1
for i in range(1, nombre + 1):
    factorial *= i

# Affichage du résultat
print(f"La factorielle de {nombre} est {factorial}")