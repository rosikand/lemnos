"""
File: mail.py
------------------
Running this script sends an email of the Lemnos list to your email. 
"""

# Important: variables you should define for yourself 
your_name = "Johnny Appleseed"  # Your name
send_username = "appleseed"  # Gmail address username to send the emails from
send_password = "johnny123"  # Password for sending email account 
receiving_address = "appleseed@gmail.com"  # Email address you'd like the emails to be sent to

import smtplib, ssl
import yagmail
from datetime import date

# path to list 
LIST_FILE_PATH = "list.txt" 

# some variables for formatting the email message 
header_all = '<h3>All items:</h3>'
header_priority = '<h3>Prioritized items:</h3>'
today = date.today()
today_string = str(today)
intro = f'Hi {your_name}, <br> <br> Here is your to-do list.'
footer = '<br> <i>This message was sent automatically with <a href="https://github.com/rosikand/lemnos">Lemnos</a>, a python-based command-line to-do list manager.</i>'

# gather contents of email (i.e. the list) 
file = open(LIST_FILE_PATH)
list_content = []
priority_list = []
for line in file:
	list_content.append(line)
	if "*" in line:
		priority_list.append(line)
email_body = [intro] + [header_priority] + priority_list + [header_all] + list_content + [footer]


# send the email 
yag = yagmail.SMTP(send_username, send_password)
subject = "To-do List: " + today_string
yag.send(receiving_address, subject, email_body)
