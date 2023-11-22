def prod(type, saison):
    if type == str(type) and saison == str(saison):
        if type == "fruits" and saison == "hiver":
            print("orange, mandarine et kiwi")
        elif type == "fruits" and saison == "ete":
            print("poire, fraise, cassis")
        elif type == "legumes" and saison == "hiver":
            print("carotte, topinambour, endive")
        elif type == "legumes" and saison == "ete":
            print("artichaut, aubergine, navet")
        else:
            print("Aucune correspondance trouvée")
    else:
        print("erreur")

prod("fruits", "hiver")
prod("fruits", "ete")
prod("legumes", "hiver")
prod("legumes", "ete")





