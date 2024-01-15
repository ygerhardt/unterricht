from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import os

main_window = CTk()
main_window.geometry("1200x800")
main_window.title("Papa Python Ristorante")
set_appearance_mode("dark")

#Images
logo_image = CTkImage(light_image=Image.open("gui\Papa python logo.png"),
                      dark_image=Image.open("gui\Papa python logo.png"),
                      size=(180,180))

menu_image= CTkImage(Image.open("gui\menu.png"), size=(20,20))


#Frames within the main_window that are on the left side in the app
frame = CTkFrame(master=main_window, width=200, height=200, border_color="grey", border_width=2, corner_radius=12)
frame.place(relx=0.01, rely=0.01)

logo_frame = CTkFrame(master=frame, width=190, height=190)
logo_frame.place(relx=0.024, rely=0.024)

logo_frame_label = CTkLabel(master = logo_frame, width=190, height=190, image=logo_image, text=None)
logo_frame_label.pack()

link_frame = CTkFrame(master=main_window, width=200, height=570, border_color="grey", border_width=2, corner_radius=12)
link_frame.place(relx=0.01, rely=0.275)

menu_frame = CTkFrame(master=link_frame, width=200,height=30)
menu_frame.place(relx=0.14, rely=0.04)

deliver_frame = CTkFrame(master=link_frame, width=200,height=30)
deliver_frame.place(relx=0.14, rely=0.11)

contact_frame = CTkFrame(master=link_frame, width=200,height=30)
contact_frame.place(relx=0.14, rely=0.18)



#Frames that are in the middle of the app
middle_frame = CTkFrame(master=main_window, width=600, height=782, border_color="grey", border_width=2, corner_radius=12) 
middle_frame.place(relx=0.185, rely=0.01)

choose_pasta_frame = CTkFrame(master=middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
choose_pasta_frame.place(relx=0.022, rely=0.01)

choose_pizza_frame = CTkFrame(master=middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
choose_pizza_frame.place(relx=0.264, rely=0.01)

choose_dessert_frame = CTkFrame(master=middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
choose_dessert_frame.place(relx=0.505, rely=0.01)

etc_frame = CTkFrame(master=middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
etc_frame.place(relx=0.746, rely=0.01)

scrollable_border_frame = CTkFrame(master=middle_frame, width=576, height=654, border_color="grey", border_width=2, corner_radius=12)
scrollable_border_frame.place(relx=0.022, rely=0.150)



food_scrollable = CTkScrollableFrame(master=scrollable_border_frame, width=542, height=628, scrollbar_button_color="#7cbfb1", scrollbar_button_hover_color="#b3e6db")
food_scrollable.place(relx=0.01, rely=0.009)



#Frames that are on the right side of the app
order_frame = CTkFrame(master=main_window, width=360, height=782, border_color="grey", border_width=2, corner_radius=12)
order_frame.place(relx=0.694,rely=0.01)

order_icon_frame = CTkFrame(master=order_frame, width=348, height=100, border_color="grey", border_width=2, corner_radius=12)
order_icon_frame.place(relx=0.016,rely=0.01)

order_scrollable_frame = CTkFrame(master=order_frame, width=348, height=580, border_color="grey", border_width=2, corner_radius=12)
order_scrollable_frame.place(relx=0.016,rely=0.15)

order_scrollable = CTkScrollableFrame(master=order_scrollable_frame, width=316, height=556, scrollbar_button_color="#7cbfb1", scrollbar_button_hover_color="#b3e6db")
order_scrollable.place(relx=0.016, rely=0.01)

payment_frame = CTkFrame(master=order_frame, width = 348, height=70, border_color="grey", border_width=2, corner_radius=12)
payment_frame.place(relx=0.016, rely=0.9)


#Buttons
menu_button = CTkButton(master=menu_frame, width=140, height=30, image=menu_image, text="Speisekarte", border_width=0, corner_radius=20, fg_color="#7cbfb1", text_color="black", hover=True, hover_color="#b3e6db")
menu_button.pack()

deliver_button = CTkButton(master=deliver_frame, width=140, height=30, text="Lieferung", border_width=0, corner_radius=20,  fg_color="#7cbfb1", text_color="black", hover=True, hover_color="#b3e6db")
deliver_button.pack()

contact_button = CTkButton(master=contact_frame, width=140, height=30, text="Kontakt", border_width=0, corner_radius=20,  fg_color="#7cbfb1", text_color="black", hover=True, hover_color="#b3e6db")
contact_button.pack()


main_window.mainloop()