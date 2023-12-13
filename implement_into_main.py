import json

with open("data/datenbank.json", "r") as datenbank:
    datenbank = json.load(datenbank)
dict_pasta = {
    "Nudelsorte": 0,
    "Sauce": 0,
    "Extrakäse": 0,
    "Scharf": 0
}


def pasta_arten():
    print("Welche Art von Pasta soll sein?")
    print(datenbank['dict_pasta'])
    input_arten = input()
    if input_arten == str(1) or input_arten == "Spaghetti":
        dict_pasta.update({"Nudelsorte": "Spaghetti"})
        pasta_sauce()
    elif input_arten == str(2) or input_arten == "Rigatoni":
        dict_pasta.update({"Nudelsorte": "Rigatoni"})
        pasta_sauce()
    elif input_arten == str(3) or input_arten == "Penne":
        dict_pasta.update({"Nudelsorte": "Penne"})
        pasta_sauce()
    else:
        print("Bitte gib eine Zahl von 1 bis 3 ein")
        pasta_arten()


def pasta_sauce():
    print("Welche Sauce darf es sein?")
    print(datenbank['dict_sauce'])
    input_sauce = input()
    if input_sauce == str(1) or input_sauce == "Tomatensauce":
        dict_pasta.update({"Sauce": "Tomatensauce"})
    elif input_sauce == str(2) or input_sauce == "Hackfleischsauce":
        dict_pasta.update({"Sauce": "Hackfleischsauce"})
    elif input_sauce == str(3) or input_sauce == "Carbonarasauce":
        dict_pasta.update({"Sauce": "Carbonarasauce"})
    elif input_sauce == str(4) or input_sauce == "Barbecuesauce":
        dict_pasta.update({"Sauce": "Barbecuesauce"})
    elif input_sauce == str(5) or input_sauce == "CremeFraichesauce":
        dict_pasta.update({"Sauce": "CremeFraichesauce"})
    else:
        print("Bitte gib eine Zahl von 1 bis 5 ein")
        pasta_sauce()
    print(dict_pasta)


print("Willkommen im Restaurant 'FIAE A'. Wir bieten Pizza und Pasta an. Was möchten Sie bestellen?")
print("1 = Pizza; 2 = Pasta")
input_gericht = input()
if input_gericht == "1" or input_gericht == "Pizza":
    print("Pizza, gute Wahl.")

elif input_gericht == "2" or input_gericht == "Pasta":
    print("Pasta, gute Wahl")
    pasta_arten()