def coup_gagnant(tas):
    """ Le coeur de la stratégie """
    modulo = tas % 5
    if modulo == 1:
        # print("je vais perdre")
        return 1  # j'éloigne le plus possible la défaite
    else:
        return (modulo + 4) % 5  # coup gagnant


def test():
    """ Un simple test de la fonction coup_gagnant()
    usage test() """
    print(coup_gagnant(10))
    print(coup_gagnant(6))
    return


test()
