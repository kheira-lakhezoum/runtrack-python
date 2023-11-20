# Programme Python pour afficher l'alphabet dans le terminal

# Boucle pour itérer à travers les lettres de 'a' à 'z'
for lettre in range(ord('a'), ord('z')+1):
    # Afficher la lettre correspondante
    print(chr(lettre), end=' ')

# Aller à la ligne après l'affichage de l'alphabet
print()
