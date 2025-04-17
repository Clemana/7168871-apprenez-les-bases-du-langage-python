import csv
def main():
    with open("input.csv", mode="r", newline='', encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        lignes = list(reader)

    salaires = []
    for ligne in lignes:
        nom = ligne["nom"]
        heures = int(ligne["heures_travaillees"])
        salaire = heures * 15
        salaires.append({"nom": nom, "salaire": salaire})

    with open("output.csv", mode="w", newline='', encoding="utf-8") as outfile:
        fieldnames = ["nom", "salaire"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(salaires)

    print("Fichier output.csv créé avec succès !")



# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
