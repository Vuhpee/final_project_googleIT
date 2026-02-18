#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
location = "supplier-data/images/"
for infile in os.listdir(location):
    if infile.endswith(".jpeg"):
        with open(location + infile, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
