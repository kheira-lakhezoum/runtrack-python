L = [3, 7, 9, 1, 2, 10, 4, 8, 5, 6]

def longueur(liste):
    compteur=0
    for i in liste:
        compteur+=1
    return compteur

def organiser(liste):   
    i=0
    while i < longueur(liste):
        j=0
        while j < (longueur(liste)-i-1):
            if liste[j] > liste[j+1]: 
                liste[j], liste[j+1] = liste[j+1], liste[j] 
            j=j+1
        i+=1    
    return liste

print(organiser(L))


