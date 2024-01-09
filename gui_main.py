from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import os

main_window = CTk()
main_window.geometry("1200x800")
main_window.title("Papa Python Ristorante")
set_appearance_mode("dark")

#Images
logo_image = CTkImage(light_image=Image.open("Papa python logo.png"),
                      dark_image=Image.open("Papa python logo.png"),
                      size=(180,180))

menu_image= CTkImage(Image.open("menu.png"), size=(20,20))


#Frames within the main_window
logo_frame = CTkFrame(master=main_window, fg_color="#242424", width=200,height=200)
logo_frame.place(relx=0.01, rely=0.01)

logo_frame_label = CTkLabel(master = logo_frame, width=200, height=200, image=logo_image, text=None)
logo_frame_label.pack()

link_frame = CTkFrame(master=main_window, width=200, height=570)
link_frame.place(relx=0.01, rely=0.275)

menu_frame = CTkFrame(master=link_frame, width=200,height=30)
menu_frame.place(relx=0.12, rely=0.04)

deliver_frame = CTkFrame(master=link_frame, width=200,height=30)
deliver_frame.place(relx=0.12, rely=0.11)

contact_frame = CTkFrame(master=link_frame, width=200,height=30)
contact_frame.place(relx=0.12, rely=0.18)


#Buttons
menu_button = CTkButton(master=menu_frame, width=140, height=30, image=menu_image, text="Speisekarte", border_width=0, corner_radius=20, fg_color="#F99A7D", text_color="black")
menu_button.pack()

deliver_button = CTkButton(master=deliver_frame, width=140, height=30, text="Lieferung", border_width=0, corner_radius=20, fg_color="#F99A7D", text_color="black")
deliver_button.pack()

contact_button = CTkButton(master=contact_frame, width=140, height=30, text="Kontakt", border_width=0, corner_radius=20, fg_color="#F99A7D", text_color="black")
contact_button.pack()


main_window.mainloop()