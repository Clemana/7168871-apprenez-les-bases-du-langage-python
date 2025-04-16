nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")
if not (nombre1.isnumeric() and nombre2.isnumeric()):
    raise SystemExit("Fin du programme")
nombre1 = int(nombre1)
nombre2 = int(nombre2)
operation = input("Entrez une opération (+, -, * ou /) : ")

if operation not in ['+', '-', '*', '/']:
    raise SystemExit("Fin du programme : opération invalide.")

if operation == '+':
    resultat = nombre1 + nombre2
elif operation == '-':
    resultat = nombre1 - nombre2
elif operation == '*':
    resultat = nombre1 * nombre2
elif operation == '/':
    if nombre2 == 0:
        raise SystemExit("Fin du programme : division par zéro impossible.")
    resultat = round(nombre1 / nombre2, 2)  

print("Résultat :", resultat)
