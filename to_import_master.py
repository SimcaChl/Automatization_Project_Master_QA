from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from selenium import webdriver
from to_import_secret_master import comandExecutor, emailPass

queryListOptimizedMonitor = ["Zanzibar", "Řecko", "Turecko", "Egypt", "Kapverdy", "Oman" , "Kefalonia", "Mirage bay", "Porto Skala 7", "Doubletree", "Magnolia", "Pegasos"]

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
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()

def setUp(self):
  #self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.driver = webdriver.Remote(
      command_executor=comandExecutor,
      desired_capabilities=desired_cap)
  #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  #webdriver.Safari(executable_path=SafariDriverManager().install())
  #generalDriverWaitImplicit(self.driver)