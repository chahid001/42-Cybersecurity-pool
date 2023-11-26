from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os

original_stdout = sys.stdout

def printUsage():
    print("./scorpion FILE1 [FILE2 ...]")
    exit(1)

def printSupport():
    print("Supported files: JPG | JPEG | PNG | GIF | BMP")

def extractMetadata(x):
    try:
        image = Image.open(x)
    except:
        print(x + ": no such file or directory.")
        return
    
    file = os.path.basename(x)
    filename = file[0:(file.find("."))] + ".metadata"
    f = open(filename, "w")
    metada = {
        "Filename": file,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }
    sys.stdout = f
    print("/////Metadata/////\n")
    for data, value in metada.items():
        print(f"{data:25}: {value}")
    exif = image.getexif()
    if exif:
        print("\n\n/////EXIF/////\n")
        for tag_id in exif:
            tag = TAGS.get(tag_id, tag_id) #get tag name from the pillow dictionnary or just stick with the defalt
            data = exif.get(tag_id) #get the value associated with the tag
            if isinstance(data, bytes): #if the data is in bytes decode it
                data = data.decode()
            print(f"{tag:25}: {data}")
    sys.stdout = original_stdout
        

def checkSuffix(argv):
    for x in argv[1:]:
        if (x.endswith(".jpg") or
            x.endswith(".jpeg") or
            x.endswith(".png") or
            x.endswith(".gif") or
            x.endswith(".bmp")):
            extractMetadata(x)
        else:
            print(x + ": not a valid file.")
             

def main():
    if len(sys.argv) < 2:
        printUsage()
    checkSuffix(sys.argv)    

main()
