L = [1, 2, 3, 4, 5]

deuxieme_valeur = L[1]
print(f"Deuxième valeur de la liste : {deuxieme_valeur}")

def mettre_a_jour():
    L[3] = L[2] + L[4]

print("Liste avant la mise à jour :", L)

mettre_a_jour()

print("Liste après la mise à jour :", L)

derniere_valeur = L[-1]
print(f"Dernière valeur de la liste : {derniere_valeur}")
