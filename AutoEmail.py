#this is an auto email sender program

#first go onto your gmail and make sure less secure is off

#import these
import smtplib
import ssl
from email.message import EmailMessage

#this is just things we need to send the email
subject = "Email from Python"
body = "This is an email from Python"
sender_email = "putyourownemail@gmail.com"
reciever_email = "putyourownemai@gmail.com"
password = input("Enter a password: ")

#this is the part where we actually build our email
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

#this basically gives a secure connection when we connect to the gmail server
context = ssl.create_default_context()

#this is to make sure the message is sending
print("Sending email...")

#this is the part where we actually send the email
#this part is where we connect to the gmail server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #now we are actually login into the server 
    server.login(sender_email, password)
    #here we are sending the messge
    #we did as string because have to convert the message we made at the top into a string
    server.sendmail(sender_email, reciever_email, message.as_string())
print("Email has been sent")

