import smtplib, ssl
from email.mime.text import MIMEText
from VARIABLES import *


def sendEmail(msg):
    fromx = 'alertserverproblem@gmail.com'
    to = 'ooo.kadoun@gmail.com'
    msg = MIMEText(msg)
    msg['Subject'] = "SRWEB1"
    msg['From'] = fromx
    msg['To'] = to

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login("alertserverproblem@gmail.com", "mamradckfischer")
    server.sendmail(fromx, to, msg.as_string())
    server.quit()

