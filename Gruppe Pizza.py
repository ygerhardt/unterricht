# Gruppe Pizza.py

from klasse_pizza import Pizza
from klasse_nudeln import Nudeln


# Klasse Pizza
meine_pizza = Pizza(2, "Salami", "Pilze", "Oliven", "Tomatensauce", True, True)
meine_pizza.essen_kochen()
print(meine_pizza)   

# Nudeln Klasse: (modul pygame, sys erforderlich. klasse_nudeln.py, nudeln_spagetti.jpg erforderlich)
meine_nudeln = Nudeln(1, "Spaghetti", "Carbonarasauce", True, False)
meine_nudeln.essen_kochen()
print(meine_nudeln)
meine_nudeln.nudeln_herstellen()
