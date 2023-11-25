from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk


root = customtkinter.CTk()
root._set_appearance_mode("dark")
root.resizable(False, False)
root.geometry('900x500')
root.title("Scorpion GUI")


frame_img = customtkinter.CTkFrame(master=root, fg_color="#5FBDFF", width=400, height=480)
frame_img.pack(side=RIGHT, padx=50, expand=True)

def open_image():
    image_path = filedialog.askopenfilename(initialdir="/", title="Select Image", 
                                            filetypes=(("PNG Images", "*.png"),))
    if image_path:
        load_image(image_path)
        return image_path

def load_image(path):
    pic = Image.open(path)
    pic = pic.resize((300,380), Image.ANTIALIAS)
    
    


button = customtkinter.CTkButton(master=frame_img, text="Add Image", command=open_image)
button_fetch = customtkinter.CTkButton(master=frame_img, text="Fetch")

image_fr = customtkinter.CTkFrame(master=frame_img, fg_color="#994D1C", width=300, height=380)
image_fr.pack(expand=True, fill=BOTH, padx=20, pady=20)
button.pack(side=RIGHT, pady=15, padx=20)
button_fetch.pack(side=LEFT, pady=15, padx=20)

frame_data = customtkinter.CTkFrame(master=root, fg_color="#994D1C", width=400, height=480)
frame_data.pack(side=LEFT, padx=50, expand=True)


    
root.mainloop()