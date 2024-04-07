# Sending an Email : send email using python
import smtplib
from tkinter import *

def send():

    sender = "ia@programmer.net"
    receiver = "Test@gmail.com"
    password = "123456789"
    subject = "Testing msg"
    body = "Writing An email.."

    #Header :
    message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

    Respond = smtplib.SMTP("smtp.google.com",587) #default mailer submission port
    Respond.starttls() #direct/tls/direct/ssl

    try:
        #login
        Respond.login(sender,password)
        print("Loged in..")
        # Sending the mail
        Respond.sendmail(sender, receiver, message)
    except smtplib.SMTPAuthenticationError:
        print("unable to login..")

    my_screen.update()
my_screen = Tk()
#===========
my_screen.config(bg="black",pady=10,padx=10)

label = Label(my_screen,font=("Comic Sans",19,"bold"),fg="gold",bg="black",
                   text="Send An Email")
label.pack(pady=10)

send = Button(my_screen,text="Send",font=("Arial",15,),fg="blue",command=send)
send.pack(pady=10)
#===========
my_screen.mainloop()