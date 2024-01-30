import json
import customtkinter
from customtkinter import *

with open("data\datenbank.json", "r") as f:
    data = json.load(f)
    
print(data["dict_pasta_sorte"]["01"])


def segmented_button_callback(value):
    print("segmented button clicked:", value)



app = CTk()
app.geometry(f"{1080}x{1080}")
set_appearance_mode("System")




app.mainloop()