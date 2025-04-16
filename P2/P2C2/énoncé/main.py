nombres = input("Entrez une liste de nombres  séparés par des virgules :")
liste = nombres.split(",")
liste_entiers = []
for element in liste:
    liste_entiers.append(int(element))

somme = sum(liste_entiers)
print("La somme est :", somme)

moyenne = somme / len(liste_entiers)
print("La moyenne est :", moyenne)

compteur = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        compteur += 1

print("Il y a", compteur, "nombres plus grands que la moyenne.")