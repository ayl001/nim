def victoire():
    """ Ceci est un programme pour jouer au jeu de Nim taquin
    et non un programme pour jouer au taquin à Nîmes """
    print("j'ai gagné !")
    exit(0)


def arbitre_coup(coup, tas):
    return (coup <= tas) and \
        (coup >= 1) and \
        (coup <= 4)


def coup_joueur(joueur, tas):
    print(f"C'est au tour de {joueur}")
    doit_jouer = True
    while doit_jouer:
        coup = int(input("Que jouez-vous ?"))
        doit_jouer = not arbitre_coup(coup, tas)
        if doit_jouer:
            print("Ce n'est pas un coup valide")
    return tas - coup
def partie(joueur1,joueur2,tas):
    joueurs=(joueur1,joueur2)
    i=0
    while tas > 0:
        tas=coup_joueur(joueurs[i],tas)
        i=1-i
        print(f"Il reste {tas} allumettes")
    print(f"{joueurs[i]} a gagné")

if __name__ == '__main__':
    joueur1: str=input("Quel est votre nom ?")
    joueur2: str=input("Quel est le nom de votre adversaire ?")
    tas=int(input("Avec combien d'allumettes jouez-vous ?"))
    partie(joueur1, joueur2, tas)