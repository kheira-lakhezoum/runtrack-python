# Création de l'inventaire avec produit, quantité et prix
nom="baguette"
quantité=20
prix_unitaire=1.20

# Affichage de l'inventaire initial
print("""nom du produit:{}, 
quantité disponible:{}, 
prix unitaire:{}""".format(nom, quantité, prix_unitaire))

# Ajout de nouveaux éléments à l'inventaire + maj de la quantité de baguette
quantité_supplementaire=int(input("quantité supplémentaire :"))
quantité+=quantité_supplementaire
print("nouveau stock",quantité)

# Augmentation tarifaire
inflation=float(prix_unitaire*1.1)
print("nouveau prix unitaire",inflation)





