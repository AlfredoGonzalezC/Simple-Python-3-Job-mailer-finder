"""
By Alfredo Gonzalez C
www.lab21online.com
contacto@lab21online.com
Version 1.15.20 (January 15th 2020)

Code for Python 3.7

"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# your credentials
email = "the gmail email to be use"
password = "the password"

# the sender's email
FROM = "the gmail email to be use"
# the receiver's email
TO   = "the target email address"
# the subject of the email (subject)
subject = "I´m Python Developer ready to relocate"

# initialize the message we wanna send
msg = MIMEMultipart()
# set the sender's email
msg["From"] = FROM
# set the receiver's email
msg["To"] = TO
# set the subject
msg["Subject"] = subject
# set the body of the email
#text = MIMEText("As a Python Programmer I use my programming skills to build tools for data analysis and automation. I am also Electronic Technician. Bilingual; fluent in English and Spanish, with a basic Portuguese level. A problem solver with excellent interpersonal skills and teaching experience, strengths in change adaptability and teamwork. Itil and Scrum knower. Portfolio link here: https://www.lab21online.com/p/diseno-de-software-y-aplicaciones-la.html  I am ready to relocate so please let me know if hiring me is an option to send you my C.V. and start the process.        Best Regards: Alfredo Gonzalez email: alfredogonzalezc@gmail.com Whatsapp: +57 3108660332 WWW.LAB21ONLINE.COM        NOTE: This is email was sent to you using a webscrapper-jobfinder-mailer-script that I coded to reach you. Check more of my projects here: https://apkpure.ai/developer/alfredo-gonzalez-c-www-lab21online-com/ ", "html")
text = '''
Warm Hi from Colombia,
    
As a Python Programmer I use my programming skills to build tools for data analysis and automation. I am also Electronic Technician. Bilingual; fluent in English and Spanish, with a basic Portuguese level. A problem solver with excellent interpersonal skills and teaching experience, strengths in change adaptability and teamwork. Itil and Scrum knower.

Embedded C++ Arduino IOT Developer, HTML, Scratch, Metasploit, Linux (Debian, Kali)

Micro-controllers coding and GUI:
https://www.youtube.com/watch?v=0JWKNR69N0o
https://www.youtube.com/watch?v=y6i7rem61pY
https://www.youtube.com/watch?v=jX0s-Rh4mAo

https://apkpure.ai/developer/alfredo-gonzalez-c-www-lab21online-com/    
https://www.lab21online.com/p/precio-del-bitcoin-hoy.html
https://www.lab21online.com/p/su-horoscopo-para-hoy.html
https://lab21-cloud-movie-database.lab21online.repl.run/

I am ready to relocate so please let me know if hiring me is an option
to send you my C.V. and start the process.

Best regards,

Alfredo Gonzalez
Whatsapp +57 3108660332

NOTE: This email was sent to you using a Webscrapper-Jobfinder-Mailer-Script 
that I coded to show you my skills. 
http://bit.ly/Script2findU

'''

text = MIMEText(text)

# attach this body to the email
msg.attach(text)
# initialize the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
# connect to the SMTP server as TLS mode (secure) and send EHLO
server.starttls()
# login to the account using the credentials
server.login(email, password)
# send the email
server.sendmail(FROM, TO, msg.as_string())
# terminate the SMTP session
server.quit()

