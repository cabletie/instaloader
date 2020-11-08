#!/usr/bin/python3
# Scales a jpg to 135 pixels max width
import PIL
from PIL import Image
basewidth = 135
img = Image.open('latest.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('latest_135.jpg’)
