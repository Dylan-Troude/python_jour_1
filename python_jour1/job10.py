investissement = 5000
rendement_annuel = 0.25 

print(f"notres investissement de base est de {investissement}, avec un rendement annuel a 25%")

new_invest = investissement * rendement_annuel + investissement

print("le rendement annuel est de : ",investissement * rendement_annuel )

print("le nouveau total est de : ",new_invest)

new_invest += 5000
rendement_annuel += 0.02

print("ajout de 5000 euros a notre investissement de" ,new_invest - 5000)

print("ce qui nous donne un investissement total de :" ,new_invest)

print(f"le rendement annuel de notre investissement de {new_invest} est de  : {new_invest * rendement_annuel} par an" )

print("le nouveau total est de notre investissement est de : ",new_invest * rendement_annuel + new_invest)

final_invest = new_invest * rendement_annuel + new_invest
final_invest *= 0.9

print("apres avoir retirer 10% de notre investisssemnt il nous reste : ",final_invest)

rendement_annuel *= 0.99
new_rendement_annuel = rendement_annuel * final_invest

print("le nouveau rendement annuel est desromais de : ", new_rendement_annuel)

print("en ajoutant le rendement annuel cela nous donne : ", new_rendement_annuel + final_invest)
