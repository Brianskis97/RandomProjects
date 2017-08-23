import getpass
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

emailserver = smtplib.SMTP('smtp.gmail.com', 587)
emailserver.ehlo()
emailserver.starttls()

ans = "n"
room = ""
user = ""
login = ""
email = ""
supervisor = ""
compname = ""
serialnum = ""
mac = " "
wall = ""
os = ""
kes = ""
ticket =  ""

Data = open("Data","w")

room = "Room: " + raw_input("What is the room?\n")
user = "Name: " + raw_input("What is the user's name?\n")
login = "Mix ID: " + raw_input("What is the user's Mix username?\n")
email = login + "@mix.wvu.edu"
supervisor = "Supervisor: " + raw_input("Who is the user's supervisor?\n")
compname = "Computer Name: " + raw_input("What is the computer's name?\n")
serialnum = "Serial Number: " + raw_input("What is the computer's serial number?\n")
mac = "MAC Address: " + raw_input("What is the computer's mac address?\n")
wall = "Wall Port: " + raw_input("Which wall port is the computer connected to?\n")
os = "OS: " + raw_input("What operating system is the computer running on\n?")
kes = "KES: " + raw_input("Is KES installed?\n")
ticket = "Ticket #:" +  raw_input("What is the RT tiket #?\n")

Data.write(room + "\n" +  user + "\n" + login + "\n" + email + "\n" + supervisor
+ "\n" + compname + "\n" + serialnum + "\n" + mac + "\n" + wall + "\n" + os + 
"\n" + kes + "\n" + ticket + "\n")

ans = raw_input("Do you want to receive this info as an email? [y/n] \n")

if (ans == "y") or (ans == "Y"):
	emailserver.login(raw_input("Please Enter your Username:\n"), getpass.getpass("Please Enter your password: \n"))
	message = MIMEMultipart('alternative')
	message['Subject'] = 'Port Activation'
	message['From'] = "brianskis97@gmail.com"
	Data = open("Data", "r")
        attach = MIMEText(Data.read())
	message.attach(attach)	
	emailserver.sendmail("brianskis97@gmail.com", "brianskis97@gmail.com", message.as_string())
else:
	print("Okay then.")
