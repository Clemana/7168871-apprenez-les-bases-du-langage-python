def salaire_mensuel(salaire_annuel):
      return salaire_annuel / 12
def salaire_hebdomadaire(salaire_mensuel) : 
      return salaire_mensuel / 4
def salaire_horaire(salaire_hebdomadaire, heures_travaillees) :
      return salaire_hebdomadaire / heures_travaillees
salaire_annuel = float(input("Saisir votre salaire annuel : "))
heures_travaillees = float(input("Saisir le nombre d'heures travaillées par semaine : "))
# Appels de fonctions
mensuel = salaire_mensuel(salaire_annuel)
hebdo = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdo, heures_travaillees)
print("Votre salaire horaire est de", round(horaire, 2), "euros")