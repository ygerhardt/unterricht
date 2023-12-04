from klasse_pizza import Pizza
from klasse_nudeln import Nudeln

# Klasse Pizza

meine_pizza = Pizza("Salami", "Pilze", "Oliven", "Barbecue")
print(meine_pizza)

meine_pizza.pizza_belegen("Schinken", "Paprika", "Hackfleisch", "Creme Fraiche")
print(meine_pizza)

# Nudeln Klasse: (modul pygame, sys erforderlich. klasse_nudeln.py, nudeln_spagetti.jpg erforderlich)
nudeln01 = Nudeln(2, 1, False, True) #Sauce, Pasta, Scharf, Extrakaese
print(nudeln01)
nudeln01.nudeln_herstellen()
