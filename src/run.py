#! /usr/bin/env python3
import os
import requests
import re

location = "supplier-data/descriptions/"
for infile in os.listdir(location):
    root, _ = os.path.splitext(infile)
    with open(location + infile) as fhand:
        line = fhand.readlines()
        json = {
        "name" : line[0].rstrip(),
        "weight" : int(re.findall(r"^[0-9]+", line[1].rstrip())[0]),
        "description" : line[2].rstrip(),
        "image_name" : root + ".jpeg"
        }
    response = requests.post("http://35.237.179.236/fruits/", json)
    response.raise_for_status()

