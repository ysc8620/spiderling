from PIL import Image
import os
img = Image.open(os.getcwd()+"/1.png")
img.save(os.getcwd()+"/.jpeg", format="jpeg")