# Gruppe Pizza.py

from klasse_pizza import Pizza
from klasse_nudeln import Nudeln


# Klasse Pizza
meine_pizza = Pizza(1, "Salami", "Pilze", "Oliven", "Tomatensauce", True, True)
print(meine_pizza.essen_kochen())

# Nudeln Klasse: (modul pygame, sys erforderlich. klasse_nudeln.py, nudeln_spagetti.jpg erforderlich)
meine_nudeln = Nudeln(1, "Spaghetti", "Carbonarasauce", False, False)
print(meine_nudeln.essen_kochen())
meine_nudeln.nudeln_herstellen()
