import random

def nombre_de_saisie():
    print("=== JEU DU NOMBRE MYSTÈRE ===")
    nombre_myster = random.randint(1, 100)
    print("DEBUG : le nombre secret est", nombre_myster)
    compteur = 0

    while True:
        saisi = input("Devine le nombre entre 1 et 100 : ")

        if not saisi.isdigit():
            print("Erreur : entre un entier, pas du texte !")
            continue

        saisi = int(saisi)

        if not 1 <= saisi <= 100:
            print("Le nombre doit être compris entre 1 et 100.")
            continue

        compteur += 1
        if saisi < nombre_myster:
            print("Le nombre mystère est plus grand !")

        elif saisi > nombre_myster:
         print("Le nombre mystère est plus petit !")

        else:
            print("Bravo ! Tu as trouvé le nombre mystère dans la", compteur, "tentative(s) !")
            break

nombre_de_saisie()