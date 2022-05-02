from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from to_import_master import setUp

URL = "https://www.fischer.sk/"
URL_poznavacky = URL+"poznavacie-zajazdy/okruhy-a-kombinovane"
URL_poznavacky_vikendy = URL+"poznavacie-zajazdy/predlzene-vikendy"
URL_poznavacky_rodiny = URL+"poznavacie-zajazdy/pre-rodiny"
URL_poznavacky_zazitky = URL+"poznavacie-zajazdy/zazitkove"
URL_pobocky = URL+"kontakty/seznam-pobocek"
URL_kluby = URL+"dovolena-animacni-kluby"
#URL_detail = URL+"/recko/zakynthos/laganas/aktypis-deluxe-sk-7?DS=1&D=623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|826|1225|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=724764&MT=3&DI=1980&RT=22&NN=7&RD=2022-09-08&DD=2022-09-01&DP=483&TO=483|1837|2933|3437&MNN=7&TT=1&PID=ZAKDSSK7&DPR=Fischer&TTM=1&TOM=483|1837|2933|3437&DF=2022-09-01|2022-09-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=0&ic1=0"
URL_detail = URL+"/grecko/rhodos/kolymbia/memphis-beach-7?DS=1&GIATA=5706&D=623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|826|1225|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=110412&MT=5&DI=13&RT=16&NN=7&RD=2022-09-13&DD=2022-09-06&DP=1837&TO=1837&MNN=7&TT=1&PID=RMEMB&DPR=Fischer&TTM=1&DF=2022-09-01|2022-09-25&ERM=0&NNM=7|8|9|10|11|12|13&ac1=2&kc1=0&ic1=0#"
#URL_SRL = URL+"vysledky-vyhledavani?d=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=653|819|724&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ac1=2"
URL_SRL = URL+"vysledky-vyhledavani?d=1009|680|953|1108|592|611|610|612|1010|590|726|609|621|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ka1=7&kc1=1&ac1=2"
URL_covidInfo = URL+"covid-info"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_fmExotika = URL+"first-minute/exotika-zima"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhledavani?tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ic1=1&ac1=2"
URL_FT_results = URL+"hladanie-vysledky?q="
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText
from to_import_secret import emailPass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

def generalDriverWaitImplicit(driver):
  driver.implicitly_wait(25)


def acceptConsent(driver):

  generalDriverWaitImplicit(driver)
  generalDriverWaitImplicit(driver)
  time.sleep(2.5)
  try:
    element = driver.execute_script(
      """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    print(element)
  except NoSuchElementException:
    print("NOSUCH")
  except TimeoutException:
    pass

  if element != None:
    element.click()

  else:
    print("consent pass")
    pass

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