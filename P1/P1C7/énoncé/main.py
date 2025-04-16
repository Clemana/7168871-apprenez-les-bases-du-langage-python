fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}
fruits['kiwi'] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
del fruits["banane"]
print("Clés restantes dans le dictionnaire :", list(fruits.keys()))
