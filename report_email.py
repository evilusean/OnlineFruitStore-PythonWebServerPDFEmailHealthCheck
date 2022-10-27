#!/usr/bin/env python3
import reports
import emails
import os
import datetime

#gets long alphanumeric username
user = os.getenv('USER')

#image directory
description_directory = '/home/{}/supplier- data/descriptions/'.format(user)

def pdf_body(input_for, desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    res = []    # names
    wt = []     # weights
    for item in os.listdir(desc_dir):
        filename = os.path.join(desc_dir, item)
        with open(filename) as f:
            line = f.readlines()
            weight = line[1].strip('\n')
            name = line[0].strip('\n')
            print(name, weight)
            res.append('name: ' + name)
            wt.append('weight: ' + weight)
            print(res)
            print(wt)

    # Initialize the object
    new_obj = ""

    # Calling values from two lists one by one.
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj


if __name__ == "__main__":
    #time= "m d, y"
    current_date = datetime.date.today().strftime("%B %d, %Y")

    #creates title with date
    title = 'Processed Update on ' + str(current_date)

    #generates report function
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf', description_directory))

    #Subject line in email
    email_subject = 'Upload Completed - Online Fruit Store'

    #body
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    #structure and send email
    msg = generate_email("automation@example.com", "{}@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")
    send_email(msg)
