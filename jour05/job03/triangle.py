# Écrire un programme qui affiche dans la console un triangle avec des ‘_’, des
# ‘\’ et des ‘/’ en fonction de l’input entré, qui représentera la hauteur.
# Exemple si l’input entré est 5 :

height=5
print(" "*(5)+"/"+"\\" )
y=1
for i in range(height-2):
    y=y+1
    print(" "*(5-i-1)+"/"+(y+i)*" "+"\\")
print(" "+"/"+(5+i+1)*"_"+"\\")
