from klasse_pizza import Pizza

pizza1 = Pizza("Salami", "Pilze", "Hackfleisch")
print(pizza1.zutat_1) 
pizza1.pizza_belegen("Schinken", "Paprika", "Oliven")
print(pizza1.zutat_2) 

print(pizza1)