from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import os

class Food_frame(CTk):
    
    def __init__(self, master, image ) -> None:
        self.parent_frame = master
        self.img = image
        self.make_frame()
    
    def make_frame(self):
        new_frame = CTkFrame(master=self.parent_frame, width=530, height=140, border_color="#7cbfb1", border_width=2, corner_radius=12)
        new_frame.pack(padx=1,pady=4)
        return new_frame
    
    def make_image_label(self):
        pass
    
    def make_order_button(self):
        pass
    
    def make_text_label(self):
        pass
    
    def make_price_label(self):
        pass
    
    def make_option_button(self):
        pass