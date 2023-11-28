# Écrire un programme qui affiche dans la console un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple :
# draw_rectangle(10, 3)

def draw_rectangle(width,height):
    print("|", width*"-", "|")
    for i in range (height -2):
        print ("|", width*" ", "|")
    print("|", width*"-", "|")

draw_rectangle(10, 3)

