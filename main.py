from PIL import Image # Open a WebP image
import glob
import os;

# utils
def getSources():
    list = glob.glob("./input/*.webp");
    return list

def prefix(name,l=0):
    name = str(name)
    if l == 0:
        return name
    for i in range(l):
        name = "0"+name;
    return name
###
webp_dir = "input"
png_dir = "output/"

os.makedirs(png_dir, exist_ok=True)
list = getSources();
i = 1
for v in list:
    name = png_dir+prefix(i,1)+".png"
    webp_image = Image.open(v)
    png_image = webp_image.convert("RGBA")
    png_image.save(name)
    i = i +1;

print("convert webp to png completed")