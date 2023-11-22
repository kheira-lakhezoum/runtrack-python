def nb(nombre):
    if type(nombre) == int and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

nb(8)
nb(15)
nb(-5)
nb("abc")

