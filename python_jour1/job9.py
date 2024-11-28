
produit = "casquette"
prix = 45
quantite = 20 

print(f"produit : {produit} ,prix: {prix} euros,  quantité disponible : {quantite}")

quantite +=  10

print("nouvelle quantité disponible" ,quantite)

x = int(input("quelle quantité voulez vous : "))

new_quantite = quantite - x

print(new_quantite)

prix = prix * 1.1 
print(prix)