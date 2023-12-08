marches=50
hauteur=10
resultat=0 

def distance(x, y):

    z = x * (y / 100) * 7 * 5 * 2
    return z

resultat = distance(marches, hauteur)

print(f"Pour {marches} marches de {hauteur} cm, le gardien parcour {resultat} metres par semaine")