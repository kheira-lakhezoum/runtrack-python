# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
# ligne/n+1 colonne traversé par une diagonale.
# Exemple pour une taille de 10 :

def tapis(n):
    print("+"+(n)*"-"+"+")
    y=1
    for i in range (n):
        y=y+1
        print ("|"+(n-i-1)*"#"+" "+(i)*"#"+"|")
    print("+"+(n)*"-"+"+")

tapis(10)