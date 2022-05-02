from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

URL = "https://www.fischer.cz/"
#URL = "https://www.fischer.sk/"
#URL = "https://www.eximtours.cz/"
#URL = "https://www.etravel.cz"
URL_poznavacky = URL+"poznavaci-zajezdy/okruzni-a-kombinovane"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy/prodlouzene-vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy/pro-rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy/zazitkove"
URL_pobocky = URL+"kontakty/seznam-pobocek"
URL_kluby = URL+"dovolena-animacni-kluby"
URL_detail = URL+"recko/rhodos/kalithea/amira?KEY=0xAC636C6ABB1245F78140DDD5CD0B0EAADE97E193&DS=1&GIATA=19462&D=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=65023&MT=2&DI=47&RT=15&NN=7&RD=2022-09-11&DD=2022-09-04&DP=4305&TO=4305&MNN=7&TT=1&PID=RPRI&DPR=Fischer&TTM=1&DF=2022-09-01|2022-09-18&ERM=0&NNM=7|8|9|10|11|12|13|17&ac1=2&kc1=1&ka1=7&ic1=0#/prehled"
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
URL_FT_results = URL+"hledani-vysledky?q="
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from selenium import webdriver
from to_import_secret_master import comandExecutor
from webdriver_manager.chrome import ChromeDriverManager

desired_cap = {
"os_version" : "14",
"device" : "iPhone 12",
"real_mobile" : "true",
"project" : "FW-full_suite",
"browserstack.local" : "false",
"browserstack.networkLogs" : "true"
}

desired_cap = {
"os" : "OS X",
"os_version" : "Monterey",
"browser" : "Safari",
"browser_version" : "15.0",
"resolution" : "1600x1200",
"project" : "ET-full_suite",
"browserstack.local" : "false",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.14.0"
}


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