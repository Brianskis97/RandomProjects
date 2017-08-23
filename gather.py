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
