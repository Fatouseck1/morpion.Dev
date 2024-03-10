import random
import time

def afficher_grille(grille):
    """ Affiche la grille de morpion """
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(grille, symbole):
    """ Vérifie s'il y a un gagnant """
    # Vérification des lignes et colonnes
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or \
           all(grille[j][i] == symbole for j in range(3)):
            return True
    # Vérification des diagonales
    if all(grille[i][i] == symbole for i in range(3)) or \
       all(grille[i][2-i] == symbole for i in range(3)):
        return True
    return False

def coup_ordinateur(grille, symbole):
    """ Choisit un coup au hasard pour l'ordinateur """
    coups_possibles = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == "-"]
    return random.choice(coups_possibles)

def coup_intelligent(grille, symbole):
    """ Choisit un coup intelligent pour l'ordinateur """
    # Priorité : vérifier s'il peut gagner
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    grille[i][j] = "-"
                    return i, j
                grille[i][j] = "-"
    # Ensuite, vérifier si l'adversaire peut gagner et le bloquer
    adversaire = "X" if symbole == "O" else "O"
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = adversaire
                if verifier_victoire(grille, adversaire):
                    grille[i][j] = "-"
                    return i, j
                grille[i][j] = "-"
    # Si aucune victoire n'est imminente, jouer un coup au hasard
    return coup_ordinateur(grille, symbole)

def morpion():
    """ Fonction principale du jeu """
    while True:
        level = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        print("Bienvenue dans le Super Morpion!")
        symboles = ["X", "O"]
        tour = 0
        while True:
            afficher_grille(level)
            symbole = symboles[tour % 2]
            print("C'est au tour du joueur", symbole)
            if symbole == "X":
                while True:
                    try:
                        ligne = int(input("Choisissez la ligne (0, 1, 2) : "))
                        colonne = int(input("Choisissez la colonne (0, 1, 2) : "))
                        if level[ligne][colonne] == "-":
                            level[ligne][colonne] = symbole
                            break
                        else:
                            print("Cette case est déjà occupée. Veuillez choisir une autre.")
                    except (ValueError, IndexError):
                        print("Veuillez entrer des coordonnées valides.")
            else:
                print("L'ordinateur réfléchit...")
                time.sleep(1)  # Pause d'une seconde pour simuler la réflexion de l'ordinateur
                ligne, colonne = coup_intelligent(level, symbole)
                level[ligne][colonne] = symbole

            if verifier_victoire(level, symbole):
                afficher_grille(level)
                if symbole == "X":
                    print("Vous avez gagné !")
                else:
                    print("L'ordinateur a gagné !")
                break
            elif all(all(c != "-" for c in ligne) for ligne in level):
                afficher_grille(level)
                print("Match nul !")
                break
            tour += 1

        rejouer = input("Voulez-vous rejouer ? (oui/non) : ")
        if rejouer.lower() != "oui":
            print("Merci d'avoir joué !")
            break

# Exécution du jeu
morpion()
