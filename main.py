import json

with open("data/datenbank.json", "r") as datenbank:
    datenbank = json.load(datenbank)

dict_pizza = {
    "Sauce": 0,
    "Zutat 1": 0,
    "Zutat 2": 0,
    "Zutat 3": 0,
    "Extrakäse": 0,
    "Scharf": 0

}

def pizza_sauce():
    print("Welche Sauce darf es sein ?")
    print(datenbank['dict_sauce'])
    input_sauce = input()
    if input_sauce == str(1) or input_sauce == "Tomatensauce":
        dict_pizza.update({"Sauce": "Tomatensauce"})
        pizza_z1()
    elif input_sauce == str(2) or input_sauce == "Hackfleischsauce":
        dict_pizza.update({"Sauce": "Hackfleischsauce"})
        pizza_z1()
    elif input_sauce == str(3) or input_sauce == "Carbonarasauce":
        dict_pizza.update({"Sauce": "Carbonarasauce"})
        pizza_z1()
    elif input_sauce == str(4) or input_sauce == "Barbecuesauce":
        dict_pizza.update({"Sauce": "Barbecuesauce"})
        pizza_z1()
    elif input_sauce == str(5) or input_sauce == "CremeFraichesauce":
        dict_pizza.update({"Sauce": "CremeFraichesauce"})
    else:
        print(" Bitte gib eine Zahl von 1 bis 5 ein")
        pizza_sauce()
        pass

def pizza_z1():
    print("Was soll die erste Zutat sein?")
    print(datenbank['dict_pizza_zutaten'])
    input_z1 = input()
    if input_z1 == str(1) or input_z1 == "Salami":
        dict_pizza.update({"Zutat 1": "Salami"})
        pizza_z2()
    elif input_z1 == str(2) or input_z1 == "Pilze":
        dict_pizza.update({"Zutat 1": "Pilze"})
        pizza_z2()
    elif input_z1 == str(3) or input_z1 == "Hackfleisch":
        dict_pizza.update({"Zutat 1": "Hackfleisch"})
        pizza_z2()
    elif input_z1 == str(4) or input_z1 == "Schinken":
        dict_pizza.update({"Zutat 1": "Schinken"})
        pizza_z2()
    elif input_z1 == str(5) or input_z1 == "Paprika":
        dict_pizza.update({"Zutat 1": "Paprika"})
        pizza_z2()
    elif input_z1 == str(6) or input_z1 == "Oliven":
        dict_pizza.update({"Zutat 1": "Oliven"})
        pizza_z2()
    else:
        print(" Bitte gib eine Zahl von 1 bis 6 ein")
        pizza_z1()
        pass


def pizza_z2():
    print("Was soll die zweite Zutat sein?")
    print(datenbank['dict_pizza_zutaten'])
    input_z1 = input()
    if input_z1 == str(1) or input_z1 == "Salami":
        dict_pizza.update({"Zutat 2": "Salami"})
        pizza_z3()
    elif input_z1 == str(2) or input_z1 == "Pilze":
        dict_pizza.update({"Zutat 2": "Pilze"})
        pizza_z3()
    elif input_z1 == str(3) or input_z1 == "Hackfleisch":
        dict_pizza.update({"Zutat 2": "Hackfleisch"})
        pizza_z3()
    elif input_z1 == str(4) or input_z1 == "Schinken":
        dict_pizza.update({"Zutat 2": "Schinken"})
        pizza_z3()
    elif input_z1 == str(5) or input_z1 == "Paprika":
        dict_pizza.update({"Zutat 2": "Paprika"})
        pizza_z3()
    elif input_z1 == str(6) or input_z1 == "Oliven":
        dict_pizza.update({"Zutat 2": "Oliven"})
        pizza_z3()
    else:
        print(" Bitte gib eine Zahl von 1 bis 6 ein")
        pizza_z2()


def pizza_z3():
    print("Was soll die dritte Zutat sein?")
    print(datenbank['dict_pizza_zutaten'])
    input_z1 = input()
    if input_z1 == str(1) or input_z1 == "Salami":
        dict_pizza.update({"Zutat 3": "Salami"})
        print(dict_pizza)

    elif input_z1 == str(2) or input_z1 == "Pilze":
        dict_pizza.update({"Zutat 3": "Pilze"})
        print(dict_pizza)

    elif input_z1 == str(3) or input_z1 == "Hackfleisch":
        dict_pizza.update({"Zutat 3": "Hackfleisch"})
        print(dict_pizza)

    elif input_z1 == str(4) or input_z1 == "Schinken":
        dict_pizza.update({"Zutat 3": "Schinken"})
        print(dict_pizza)

    elif input_z1 == str(5) or input_z1 == "Paprika":
        dict_pizza.update({"Zutat 3": "Paprika"})
        print(dict_pizza)

    elif input_z1 == str(6) or input_z1 == "Oliven":
        dict_pizza.update({"Zutat 3": "Oliven"})
        print(dict_pizza)

    else:
        print(" Bitte gib eine Zahl von 1 bis 6 ein")
        pizza_z3()


print("willkommen im Restaurant 'FIAE A'. Wir bieten Pizza und Pasta an. Was möchten Sie bestellen ?")
print("1 = Pizza; 2 = Pasta")
input_gericht = input(str())


if input_gericht == "1" or input_gericht == "Pizza":
    print("Pizza, gute Wahl.")
    pizza_sauce()





if input_gericht == "2" or input_gericht == "Pasta":
    print("Pasta gute Wahl")
