n = int(input("Tapez la valeur : "))
print("La table de multiplication de ", n," est :")

for i in range(1, n+1):
    print(f"Table de multiplication de {i} :")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} * {j} = {resultat}")