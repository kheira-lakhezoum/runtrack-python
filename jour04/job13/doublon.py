L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def doublons(list):
    print(f"Liste avant suppression des doublons : {L}")
    liste_bis = [] 

    for i in list:
        if i not in liste_bis:
            liste_bis += [i]
    return liste_bis

print(f"Liste après suppression des doublons : {doublons(L)}")