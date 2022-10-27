#!/usr/bin/env python3

from PIL import Image
import os
import sys

#gets long alphanumeric username
user = os.getenv('USER')

#image directory
image_directory = '/home/{}/supplier-data/images/'.format(user)

for image_name in os.listdir(image_directory):
    #ignores images that don't have .tiff format
    if not image_name.startswith('.') and 'tiff' in image_name:

        #creates path variable
        image_path = image_directory + image_name

        #split and take first indexed part
        path = os.path.splitext(image_path)[0]

        #Open the image
        im = Image.open(image_path)

        #create new path with jpeg format
        new_path = '{}.jpeg'.format(path)

        #resize and then save it as jpeg
        im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")
