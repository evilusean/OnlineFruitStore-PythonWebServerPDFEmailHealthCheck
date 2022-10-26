# OnlineFruitStore-PythonWebServerPDFEmailHealthCheck

## By Google/Sean With Coursera/Qwiklabs 

## Project Scenario:
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

### What you'll do:
* Write a script that summarizes and processes sales data into different categories
* Generate a PDF using Python
* Automatically send a PDF by email
* Write a script to check the health status of the system


## Project Writeup:

### Fetching supplier data/Resizing Images:

`changeImage.py`

You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Run `download_drive_file.sh` to download a file named `supplier-data.tar.gz`. Extracted using 'tar xf ~/supplier-data.tar.gz' in shell.
This creates a directory named `supplier-data`, that contains subdirectories named `images` and `descriptions`.

The subdirectory `images` contain images of various fruits, while the `descriptions` subdirectory has text files containing the description of each fruit.

[CODE IMAGE]

Here is the code used for a python script used to process the supplier images. It uses the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

* Size: Change image resolution from 3000x2000 to 600x400 pixel
* Format: Change image format from .TIFF to .JPEG

### Uploading images to web server:

`supplier_image_upload.py`

You have modified the fruit images through `changeImage.py` script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the upload URL.

[CODE IMAGE]

The Python script above, takes the jpeg images from the `supplier-data/images` directory that you've processed previously and uploads them to the web server fruit catalog.

[UPDATED WEBSERVER IMAGE]

## Googles IT Automation With Python Final Project: Online Fruit Store

https://www.coursera.org/professional-certificates/google-it-automation

Full Course Documentation: 

https://github.com/evilusean/CourseraGoogle/tree/main/IT-Automation-With-Python

Project Documentation:

https://github.com/evilusean/CourseraGoogle/tree/main/IT-Automation-With-Python/6Automating%20Real-World%20Tasks%20with%20Python

## Packages/Modules Used in project:

Linux/Shell Environment.

Python:

Python Image Library (PIL) - For Image Manipulation

Requests (HTTP client library) 

ReportLab (PDF creation library)

email (constructing email)

smtplib (sending email)

os(interacts with operating sytem)

sys(provides various functions and variables that are used to manipulate different parts of the Python runtime environment.)

psutil(process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization)

shutil — High-level file operations(system checks - disk usage)
