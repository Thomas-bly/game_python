import random

def lancer_des():
    return random.randint(1, 9)

def calculer_points(joueur, valeur_des):
    points = 0
    if valeur_des == 1:
        points = -1
    elif valeur_des == 2:
        points = 2
    elif valeur_des == 3:
        points = 3
        while True:
            valeur_des = lancer_des()
            if valeur_des != 3:
                break
            points += 3
    elif valeur_des == 4:
        points = 5
    elif valeur_des == 5:
        points = 4
    elif valeur_des == 6:
        points = 6
        while True:
            valeur_des = lancer_des()
            if valeur_des != 6:
                break
            points -= 6
    elif valeur_des == 7:
        points = 7
    elif valeur_des == 8:
        points = -10
    elif valeur_des == 9:
        points = 18
    return points

def jouer():
    scores = {'ALPHA': 0, 'OMEGA': 0}
    joueur_courant = 'ALPHA'
    while True:
        commande = input("Entrez 'go' pour lancer le dés: ")
        if commande == 'go':
            valeur_des = lancer_des()
            points = calculer_points(joueur_courant, valeur_des)
            scores[joueur_courant] += points
            print(f"{joueur_courant} a lancé un {valeur_des} et a obtenu {points} points. Scores: ALPHA {scores['ALPHA']}, OMEGA {scores['OMEGA']}")
            if scores[joueur_courant] >= 30:
                print(f"{joueur_courant} a gagné !")
                break
            joueur_courant = 'OMEGA' if joueur_courant == 'ALPHA' else 'ALPHA'

jouer()