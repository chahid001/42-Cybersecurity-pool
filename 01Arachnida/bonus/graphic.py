import scorpion
from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image
from PIL.ExifTags import TAGS



root = customtkinter.CTk()
root._set_appearance_mode("dark")
root.resizable(False, False)
root.geometry('1200x600')
root.title("Scorpion GUI")


frame_img = customtkinter.CTkFrame(master=root, fg_color="#27374D", width=400, height=480)
frame_img.pack(side=RIGHT, padx=50, expand=True)
image_label = None
path = None
metadata_label = None

def open_image():
    global path
    image_path = filedialog.askopenfilename(initialdir="/", title="Select Image", 
                                            filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg"),
                                                       ("JPEG Images", "*.jpeg"), ("GIF Images", "*.gif"), 
                                                       ("BMP Images", "*.bmp"),))
    if image_path:
        path = image_path
        load_image(image_path)

def load_image(path):
    global image_label
    pic = Image.open(path)
    pic = customtkinter.CTkImage(light_image=pic, size=(300, 360))
    
    if image_label:
        image_label.configure(image=pic)
        image_label.image = pic
    else:
        image_label = customtkinter.CTkLabel(master=image_fr, image=pic, text="")
        image_label.pack()
    
def fetch_metadata():
    global metadata_label
    if image_label:
        image = Image.open(path)
        metadata = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        if metadata_label:
            metadata_label.destroy()
        metadata_label = customtkinter.CTkLabel(master=frame_data, text="")
        metadata_label.grid(row=0, column=0, sticky="w")
        index = 0
        for data, value in metadata.items():
            label = customtkinter.CTkLabel(master=metadata_label, text=f"{data}: {value}\n")
            label.grid(row=index+1, column=0, sticky="w")
            index = index + 1

        exif = image.getexif()
        if exif:
            # label = customtkinter.CTkLabel(master=metadata_label, text="EXIF Data")
            # label.grid(row=index+2, column=0, sticky="w")
            for tag_id in exif:
                tag = TAGS.get(tag_id, tag_id) #get tag name from the pillow dictionnary or just stick with the defalt
                data = exif.get(tag_id) #get the value associated with the tag
                if isinstance(data, bytes): #if the data is in bytes decode it
                    data = data.decode()
                label = customtkinter.CTkLabel(master=metadata_label, text=f"{tag:10}: {data}\n")
                label.grid(row=index+1, column=0, sticky="w")
                index = index + 1


    else:
        return


button = customtkinter.CTkButton(master=frame_img, text="Add Image", command=open_image,)
button_fetch = customtkinter.CTkButton(master=frame_img, text="Fetch", command=fetch_metadata,)

image_fr = customtkinter.CTkFrame(master=frame_img, fg_color="#27374D", width=300, height=380)
image_fr.pack(expand=True, fill=BOTH, padx=20, pady=20)
button.pack(side=RIGHT, pady=15, padx=20)
button_fetch.pack(side=LEFT, pady=15, padx=20)

frame_data = customtkinter.CTkScrollableFrame(master=root, fg_color="#27374D", width=600, height=480)
frame_data.pack(side=LEFT, padx=50, expand=True)


    
root.mainloop()