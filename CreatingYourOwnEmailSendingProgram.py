#Creating Your Own Email Sending Program


import smtplib as mailer
from getpass import getpass
#Connection to SMTP Server
Connection = mailer.SMTP('smtp.gmail.com',587) #establishing connection to gmail smtp server
Connection.ehlo() #this will connect to the gmail
Connection.starttls() #this will allow the encryption

#Login Details
try: 
	LoginDetailsFile = open('.\LoginDetailsMailer.txt','r')	
	Content = LoginDetailsFile.readlines()
	SenderMail = Content[0]
	SenderPassword = Content[1]
	Search =Connection.login(SenderMail,SenderPassword) #Logining to the username and password provided by the user

except: 
	SenderMail = input('Enter Your Gmail Address: ')
	SenderPassword = getpass('Enter Your Gmail Password: ')
	Connection.login(SenderMail,SenderPassword) #Logining to the username and password provided by the user


#Sender Details
SendingTo = input("Enter the Sending To Address: ")
Subject = input("Enter the Subject Of Email: ")
Body = input("Enter The Body of the Mail: ")

#Send Mail
Connection.sendmail(SenderMail,SendingTo,'Subject: '+str(Subject)+'\n\n'+str(Body))

#Display In Console
print('Message Sent Successfuly')

#Exiting Mailer
Connection.quit()
