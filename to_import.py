from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

URL = "https://www.fischer.cz/"
#URL = "https://www.eximtours.cz/"
#URL = "https://www.etravel.cz"
URL_poznavacky = URL+"poznavaci-zajezdy/okruzni-a-kombinovane"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy/prodlouzene-vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy/pro-rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy/zazitkove"
URL_pobocky = URL+"kontakty/seznam-pobocek"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_detail = URL+"recko/lefkada/agios-nikitas/olive-tree-ct?DS=1&D=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=628177&MT=1&DI=49&RT=15&NN=7&RD=2022-08-18&DD=2022-08-11&DP=4305&TO=4305&MNN=7|8|9|10|11&TT=1&PID=LFOLISO&DPR=Fischer&TTM=1&DF=2022-08-11|2022-09-11&ERM=0&NNM=7|8|9|10|11&ac1=2&kc1=0&ic1=0#"
#URL_SRL = URL+"vysledky-vyhledavani?d=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
URL_covidInfo = URL+"covid-info"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_fmExotika = URL+"first-minute/exotika-zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhledavani?tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ic1=1&ac1=2"
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret import emailPass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def setUp(self):
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  #self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
  #self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
  #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def tearDown(self):
  self.driver.quit()

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

def acceptConsent(driver):
  time.sleep(2)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  except NoSuchElementException:
    return

  except TimeoutException:
    pass
  try:
    element.click()
  except TimeoutException:
    pass
  except NoSuchElementException:
    return

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
      exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
      if exponeaBanner.is_displayed():
        wait.until(EC.visibility_of(exponeaBanner))
        exponeaCrossAndBanner = driver.find_element_by_xpath(
          "//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
        exponeaCrossAndBanner.click()
        time.sleep(2)

    except NoSuchElementException:
      print("nenasle se exponea banner")

def acceptConsent3(driver):
  time.sleep(2)

  element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
  if element !=0:

      pass

  else:
      element.click()


desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"browserstack.local" : "false",
"browserstack.selenium_version" : "3.5.2"
}