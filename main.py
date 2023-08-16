from smtplib import *
import datetime as dt
import random

#--------------------Date----------------#
date = dt.datetime.now()
day = date.weekday()

#--------------------Email and password----------------#
my_email = input('Sender email: ')
password = input("Password: ")
send_to =input("Send to: ")

#--------------opening quotes-------------------#
with open("quotes.txt") as file:
    quote = file.readlines()  
msg = f'Subject:Motivation quote\n\nDear {send_to.replace("@gmail.com","")},\n\nQuote od the day: {random.choice(quote)}' 


#-------------Conditional statement---------------#
if day == 4:
    with  SMTP('smtp.gmail.com',587,timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=send_to,msg=msg)
        print("email send.")

print(day)