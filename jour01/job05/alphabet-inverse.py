# Programme Python pour afficher l'alphabet à l'envers dans le terminal

# Boucle pour itérer à travers les lettres de 'z' à 'a' en ordre décroissant
for lettre in range(ord('z'), ord('a')-1, -1):
    # Afficher la lettre correspondante
    print(chr(lettre), end=' ')

# Aller à la ligne après l'affichage de l'alphabet à l'envers
print()
