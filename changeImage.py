#!/usr/bin/env python3
from PIL import Image
import os

location = "supplier-data/images/"
for infile in os.listdir(location):
    if infile.endswith(".tiff"):
        file, ext = os.path.splitext(infile)
        with Image.open(location + infile) as im:
            im.resize((600,400)).convert("RGB").save(location + file + ".jpeg")
        os.remove(location + infile)