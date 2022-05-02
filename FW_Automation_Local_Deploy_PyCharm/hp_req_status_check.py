import http
import smtplib
from email.mime.text import MIMEText

from urllib3 import Retry

from to_import import URL, sendEmail
import requests
import time
from to_import_secret import emailPass
mujMail = 'ooo.kadoun@gmail.com'
filipMail = 'filip.rytych@seznam.cz'

def sendEmailv2(msg, recipient):
  fromx = 'alertserverproblem@gmail.com'
  to = recipient
  msg = MIMEText(msg)
  msg['Subject'] = "HP CHECK"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()
pocetChecku = 0
while True:
    URL = "https://fischer.web1.dtweb.cz"
    #response = requests.get(URL)
    time.sleep(2)

    try:

        response = requests.get(URL)
        if response.status_code == 500:
            msg = "FW HP 500, SRWEB1"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)

        if response.status_code == 404:
            msg = "FW HP 404, SRWEB1"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)
    #except requests.exceptions.ConnectionError:
    except:
        pass
    print(URL)
    print(response.status_code)

    time.sleep(2)
    URL = "https://fischer.web2.dtweb.cz"
    try:
        response = requests.get(URL)
        if response.status_code == 500:
            msg = "FW HP 500, SRWEB2"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)

        if response.status_code == 404:
            msg = "FW HP 404, SRWEB2"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)
    #except requests.exceptions.ConnectionError:
    except:
        pass
    print(URL)
    print(response.status_code)

    time.sleep(2)
    URL = "https://fischer.web3.dtweb.cz"
    try:
        response = requests.get(URL)
        if response.status_code == 500:
            msg = "FW HP 500, SRWEB3"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)

        if response.status_code == 404:
            msg = "FW HP 404, SRWEB3"
            sendEmailv2(msg, mujMail)
            sendEmailv2(msg, filipMail)
    #except requests.exceptions.ConnectionError:
    except:
        pass
    print(URL)
    print(response.status_code)


    pocetChecku = pocetChecku+1
    print("CHECK NUMERO  " + str(pocetChecku))
    print("CHECK NUMERO  " + str(pocetChecku))
    print("CHECK NUMERO  " + str(pocetChecku))
    time.sleep(33)