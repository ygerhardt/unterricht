import customtkinter 
import webbrowser
from customtkinter import *
from tkinter import *
from PIL import Image
import os


customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def setze_root_verzeichnis():
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath) 
        os.chdir(dname) 

    def __init__(self):
        super().__init__()
        
        self.geometry(f"{1200}x{800}")
        self.title("Restaurant FIAE")
        
        
        #Images
        logo_image = CTkImage(light_image=Image.open("gui\pictures\Papa python logo.png"),
                              dark_image=Image.open("gui\pictures\Papa python logo.png"),
                              size=(180,180))

        pizza_label_icon = CTkImage(Image.open("gui\\pictures\\icons\\pizza_icon.png"), size=(60,60))
        pasta_label_icon = CTkImage(Image.open("gui\\pictures\\icons\\pasta_icon.png"), size=(60,60))
        dessert_label_icon = CTkImage(Image.open("gui\\pictures\\icons\\dessert_icon.png"), size=(60,60))
        other_label_icon = CTkImage(Image.open("gui\\pictures\\icons\\beverage_icon.png"), size=(60,60))
        


        #Frames within the main_window that are on the left side in the app
        self.frame = CTkFrame(master=self, width=200, height=200, border_color="grey", border_width=2, corner_radius=12)
        self.frame.place(relx=0.01, rely=0.01)

        self.logo_frame = CTkFrame(master=self.frame, width=190, height=190)
        self.logo_frame.place(relx=0.024, rely=0.024)

        self.logo_frame_label = CTkLabel(master = self.logo_frame, width=190, height=190, image=logo_image, text=None)
        self.logo_frame_label.pack()

        self.link_frame = CTkFrame(master=self, width=200, height=570, border_color="grey", border_width=2, corner_radius=12)
        self.link_frame.place(relx=0.01, rely=0.275)
        
        self.switch_frame = CTkFrame(master=self.link_frame, width=180,height=60, border_color= "grey", border_width=2, corner_radius=12)
        self.switch_frame.place(relx=0.048, rely=0.88)
        
        self.light_mode_switch_frame =CTkFrame(master=self.switch_frame, width=180,height=160, border_color= "grey", border_width=2, corner_radius=12)
        self.light_mode_switch_frame.place(relx=0.030, rely=0.074)
        
        self.contact_frame = CTkFrame(master=self.link_frame, width=200,height=30)
        self.contact_frame.place(relx=0.14, rely=0.18)

     #Frames that are in the middle of the app
        self.middle_frame = CTkFrame(master=self, width=600, height=782, border_color="grey", border_width=2, corner_radius=12) 
        self.middle_frame.place(relx=0.185, rely=0.01)

        #pizza frame
        self.choose_pizza_frame = CTkFrame(master=self.middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
        self.choose_pizza_frame.place(relx=0.264, rely=0.01)
        self.pizza_icon_frame=CTkFrame(master=self.choose_pizza_frame, width=80, height=80)
        self.pizza_icon_frame.place(relx=0.028,rely=0.05)
        self.pizza_label=CTkLabel(master=self.pizza_icon_frame, image=pizza_label_icon, width=132, height=90, text="", cursor ="hand2")
        self.pizza_label.bind("<Button-1>", self.open_url, True)
        self.pizza_label.pack()
        
        #pasta frame
        self.choose_pasta_frame = CTkFrame(master=self.middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
        self.choose_pasta_frame.place(relx=0.022, rely=0.01)
        self.pasta_icon_frame=CTkFrame(master=self.choose_pasta_frame, width=80, height=80)
        self.pasta_icon_frame.place(relx=0.028,rely=0.05)
        self.pizza_label=CTkLabel(master=self.pasta_icon_frame, image=pasta_label_icon, width=132, height=90, text="", cursor ="hand2")
        self.pizza_label.bind("<Button-1>", self.open_url, True)
        self.pizza_label.pack()
        
        #dessert frame
        self.choose_dessert_frame = CTkFrame(master=self.middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
        self.choose_dessert_frame.place(relx=0.505, rely=0.01)
        self.dessert_icon_frame=CTkFrame(master=self.choose_dessert_frame, width=80, height=80)
        self.dessert_icon_frame.place(relx=0.028,rely=0.05)
        self.dessert_label=CTkLabel(master=self.dessert_icon_frame, image=dessert_label_icon, width=132, height=90, text="", cursor ="hand2")
        self.dessert_label.bind("<Button-1>", self.open_url, True)
        self.dessert_label.pack()

        #other frame
        self.choose_etc_frame = CTkFrame(master=self.middle_frame, width=140, height=100, border_color="grey", border_width=2, corner_radius=12) 
        self.choose_etc_frame.place(relx=0.746, rely=0.01)
        self.etc_icon_frame=CTkFrame(master=self.choose_etc_frame, width=80, height=80)
        self.etc_icon_frame.place(relx=0.028,rely=0.05)
        self.etc_label=CTkLabel(master=self.etc_icon_frame, image=other_label_icon, width=132, height=90, text="", cursor ="hand2")
        self.etc_label.bind("<Button-1>", self.open_url, True)
        self.etc_label.pack()

        self.scrollable_border_frame = CTkFrame(master=self.middle_frame, width=576, height=654, border_color="grey", border_width=2, corner_radius=12)
        self.scrollable_border_frame.place(relx=0.022, rely=0.150)

        #Food Scrollable 
        self.food_scrollable = CTkScrollableFrame(master=self.scrollable_border_frame, width=542, height=628, scrollbar_button_color="#7cbfb1", scrollbar_button_hover_color="#b3e6db")
        self.food_scrollable.place(relx=0.01, rely=0.009)

        #Frames that are on the right side of the app
        self.order_frame = CTkFrame(master=self, width=360, height=782, border_color="grey", border_width=2, corner_radius=12)
        self.order_frame.place(relx=0.694,rely=0.01)

        self.order_icon_frame = CTkFrame(master=self.order_frame, width=348, height=100, border_color="grey", border_width=2, corner_radius=12)
        self.order_icon_frame.place(relx=0.016,rely=0.01)

        self.order_scrollable_frame = CTkFrame(master=self.order_frame, width=348, height=580, border_color="grey", border_width=2, corner_radius=12)
        self.order_scrollable_frame.place(relx=0.016,rely=0.15)

        self.order_scrollable = CTkScrollableFrame(master=self.order_scrollable_frame, width=316, height=556, scrollbar_button_color="#7cbfb1", scrollbar_button_hover_color="#b3e6db")
        self.order_scrollable.place(relx=0.016, rely=0.01)

        self.payment_frame = CTkFrame(master=self.order_frame, width = 348, height=70, border_color="grey", border_width=2, corner_radius=12)
        self.payment_frame.place(relx=0.016, rely=0.9)


        #Button
        self.contact_button = CTkButton(master=self.contact_frame, 
                                        width=140, 
                                        height=30, 
                                        text="Kontakt", 
                                        border_width=3,
                                        border_color="#0a5c5c", 
                                        corner_radius=20,  
                                        fg_color="#7cbfb1", 
                                        text_color="black",
                                        hover=True, 
                                        hover_color="#b3e6db")
        self.contact_button.pack()
        
        self.light_mode_switch = CTkSwitch(master=self.light_mode_switch_frame, 
                                           width=170, height=50, 
                                           fg_color="#0a5c5c", progress_color="#7cbfb1", text="Light Mode", 
                                           switch_height=20,switch_width=40,
                                           border_width=2, border_color="grey", corner_radius=12,
                                           command=self.switch_to_light_mode)
        self.light_mode_switch.pack() 
        
    def switch_to_light_mode(self):
        button_value = self.light_mode_switch.get()
        while button_value==1 or button_value ==0:
            button_value = self.light_mode_switch.get()
            if button_value == 1:
                return set_appearance_mode("light")
            else:
                return  set_appearance_mode("dark")
            
    def open_url(self,CTk):
        link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.open(link)
        
       

if __name__ == "__main__":
    App.setze_root_verzeichnis
    app = App()
    app.mainloop()