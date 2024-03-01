def afficher_grille(level):
    for ligne in level:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(level, symbole):
    for i in range(3):
        if level[i] == [symbole] * 3 or [level[j][i] for j in range(3)] == [symbole] * 3:
            return True

    if [level[i][i] for i in range(3)] == [symbole] * 3 or [level[i][2-i] for i in range(3)] == [symbole] * 3:
        return True

    return False

def morpion():
    while True:
        print("Bienvenue dans le Super Morpion!")
        level = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        symboles = ["X", "O"]
        tour = 0
        while True:
            afficher_grille(level)
            symbole = symboles[tour % 2]
            print("C'est au tour du joueur", symbole)
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
            if verifier_victoire(level, symbole):
                afficher_grille(level)
                print("Le joueur", symbole, "a gagné !")
                break
            elif all(all(c != "-" for c in ligne) for ligne in level):
                afficher_grille(level)
                print("Match nul !")
                break
            tour += 1
        rejouer = input("Voulez-vous refaire une partie ? (o/n) : ")
        if rejouer.lower() != "o":
            break

# Exécution du jeu
morpion()
