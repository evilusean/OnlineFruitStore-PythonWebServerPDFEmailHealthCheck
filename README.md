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

To download the file from the supplier onto our linux-instance virtual machine we will first grant executable permission to the `download_drive_file.sh` script.

`sudo chmod +x ~/download_drive_file.sh`

Run the download_drive_file.sh shell script with the following arguments

`./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz`

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/1supplier-dataImg.png?raw=true"</center>  
</p>

Run `download_drive_file.sh` to download a file named `supplier-data.tar.gz`. Extracted using `tar xf ~/supplier-data.tar.gz` in shell.
This creates a directory named `supplier-data`, that contains subdirectories named `images` and `descriptions`.

The subdirectory `images` contain images of various fruits, while the `descriptions` subdirectory has text files containing the description of each fruit.

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/2changeImage.jpg"</center>  
</p>

Here is the code used for a python script used to process the supplier images. It uses the PIL library to update all images within `~/supplier-data/images` directory to the following specifications:

* Size: Change image resolution from 3000x2000 to 600x400 pixel
* Format: Change image format from .TIFF to .JPEG

### Uploading images to web server:

`supplier_image_upload.py`

You have modified the fruit images through `changeImage.py` script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the upload URL.

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/3supplier_image_upload.jpg"</center>  
</p>

The Python script above, takes the jpeg images from the `supplier-data/images` directory that you've processed previously and uploads them to the web server fruit catalog. 

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/4WebServerImagesUploaded.jpg"</center> 
</p>

### Uploading the descriptions:

`run.py`

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/5run.jpg"</center> 
</p>

The Django server is already set up to show the fruit catalog for your company. To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the fruit images and their respective description in JSON format.

Write a Python script named `run.py` to process the text files (001.txt, 003.txt ...) from the `supplier-data/descriptions` directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to the webserver using the Python requests library.

Now, you'll have to process the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/ directory and save them in a data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:

* name
* weight (in lbs)
* description

The data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

The image_name field will allow the system to find the image associated with the fruit. Don't forget to add all fields, including the image_name! The final JSON object should be similar to:
`{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}`
Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL webserver.

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/6WebServerFruitDescriptionUpdate.jpg"</center> 
</p>

### Generate a PDF Report and send through an Email:

`reports.py`

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/7reports.jpg"</center> 
</p>

`report_email.py`

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/8report_email.jpg"</center> 
</p>

Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:

Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]

Using the reportlab Python library, define the method generate_report to build the PDF reports.

Create another script named `report_email.py` to process supplier fruit description data from `supplier-data/descriptions` directory.

Import all the necessary libraries(`os`, `datetime` and `reports`) that will be used to process the text data from the `supplier-data/descriptions` directory into the format below:

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]

...

Once you have completed this, call the main method which will process the data and call the `generate_report` method from the `reports` module:

You will need to pass the following arguments to the `reports.generate_report` method: the text description processed from the text files as the `paragraph` argument, the report title as the `title` argument, and the file path of the PDF to be generated as the `attachment` argument (use `‘/tmp/processed.pdf'`)

### Send Report Through an Email:

`emails.py`

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/9emails.jpg"</center> 
</p>

Once the PDF is generated, you need to send the email using the `emails.generate_email()` and `emails.send_email()` methods.
Define generate_email and send_email methods by importing necessary libraries.
Use the following details to pass the parameters to emails.generate_email():
* From: automation@example.com
* To: username@example.com
* Replace username with the username given in the Connection Details Panel on the right hand side.
* Subject line: Upload Completed - Online Fruit Store
* E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
* Attachment: Attach the path to the file processed.pdf

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/10WebMailPDFReport.jpg"</center> 
</p>

### Health check:

`health_check.py`

This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

* Report an error if CPU usage is over 80%
* Report an error if available disk space is lower than 20%
* Report an error if available memory is less than 500MB
* Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:

From: automation@example.com
To: username@example.com
Replace username with the username given in the Connection Details Panel on the right hand side.
Subject line:
Case

Case | Subject line
------------- | -------------
CPU usage is over 80% | Error - CPU usage is over 80%
Available disk space is lower than 20% | Error - Available disk space is less than 20%
available memory is less than 500MB | Error - Available memory is less than 500MB
hostname "localhost" cannot be resolved to "127.0.0.1" | Error - localhost cannot be resolved to 127.0.0.1

E-mail Body: Please check your system and resolve the issue as soon as possible.

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/11healthcheck.jpg"</center> 
</p>

Note: There is no attachment file here, so you must be careful while defining the generate_email() method in the emails.py script or you can create a separate generate_error_report() method for handling non-attachment email.

Next, go to the webmail inbox and refresh it. There should only be an email something goes wrong, so hopefully you don't see a new email.

To test out your script, you can install the `stress` tool.

`sudo apt install stress`

#Next, call the tool using a good number of CPUs to fully load our CPU resources:

`stress --cpu 8`

Allow the stress test to run, as it will maximize our CPU utilization. Now run health_check.py by opening another SSH connection to the linux-instance. Navigate to Accessing the virtual machine on the navigation pane on the right-hand side to open another connection to the instance.

Check your inbox for any new email.

<p align="center">  
<img src="https://github.com/evilusean/OnlineFruitStore-PythonWebServerPDFEmailHealthCheck/blob/main/Images/12StressCPUEmail.jpg"</center> 
</p>

Now, you will be setting a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user.

To set a user cron job use the following command:

`crontab -e`

health_check.py now runs every 60 seconds!

Congratulations!

Congrats! You've successfully created a python script that processes images and descriptions and then updates your company's online website to add the new products. You have also generated a PDF report and sent it by email. Finally, you have also set up monitoring of the system's health.

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

datetime(for PDF report)

email (constructing email)

smtplib (sending email)

os(interacts with operating sytem)

sys(provides various functions and variables that are used to manipulate different parts of the Python runtime environment.)

psutil(process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization)

shutil — High-level file operations(system checks - disk usage)
