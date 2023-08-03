from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from webdriver_manager.chrome import ChromeDriverManager

from to_import_secret_master import emailPass, comandExecutor
from selenium import webdriver


brand_name_project = "EXIM"

desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized - Web Monitor V2",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}
def setUp(self):
  #self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False


#URL = "https://www.eximtours.cz/"
#URL = "https://exim.stg.dtweb.cz/"
URL = "http://eximpl.web11.dtweb.cz/"
URL_poznavacky = URL+"poznavaci-zajezdy"
URL_poznavacky_vikendy = URL+"poznavaci-zajezdy#vikendy"
URL_poznavacky_rodiny = URL+"poznavaci-zajezdy#rodiny"
URL_poznavacky_zazitky = URL+"poznavaci-zajezdy#rodiny"
URL_pobocky = URL+"kontakty/nase-pobocky"
URL_kluby = URL+"informace-pro-klienty/mango-club"
#URL_detail = URL+"/egypt/hurghada/hurghada/hawaii-caesar-palace-egypt-2?AC1=2&D=64419|64420|64421|64422|64423|64424|64425|64426&DD=2023-06-06&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=411448&HID=9198&IC1=0&KC1=0&MNN=7&MT=5&NN=7&PID=HRG90006&RD=2023-06-13&TO=4305&acm1=2&df=2023-06-01|2023-06-30&nnm=7|8|9|10|11|12|13&tt=1&ttm=1#/prehled"
#URL_detail = URL + "/turecko/turecka-riviera/avsallar/incekum-su?D=63260|63288|63448|64152|64153|64154|64157|211801|211814&DD=2023-08-28&DP=4305&DPR=EXIM+TOURS+ATCOM&DS=8192&GIATA=59394&HID=374&MNN=7&MT=5&NN=7&PID=AYT19071&RD=2023-09-04&TO=4305&df=2023-08-21|2023-09-30&nnm=7|8|9|10|11|12|13&sortby=Departure&tt=1&ttm=1#/prehled"
URL_detail = URL +"/hiszpania/costa-brava/lloret-de-mar/blue-sea-montevista-hawai?AC1=2&D=63213|63226|63241|63242|63243|63245|63284|63350|63455|74459|74460|74465&DD=2023-09-14&DP=1149&DPR=EXIM+TOURS+POLAND&DS=1024&GIATA=2346&HID=11100&IC1=0&IFM=0&ILM=0&KC1=0&KEY=2691407240&MMT=5&MNN=6&MT=5&NN=6&PID=34141&RD=2023-09-20&RT=15&acm1=2&df=2023-09-01|2023-09-30&nnm=6|7|8|9|10|11|12|13|14&tt=1&ttm=1#/prehled"
#URL_SRL = URL + "/vysledky-vyhledavani?ac1=2&d=64087|64094|64095|64089|64090|64091|64086|64092&dd=2023-05-01&nn=7|8|9|10|11|12|13&rd=2023-06-30&to=4312|4305|2682|4308&tt=1 "
URL_covidInfo = URL+"covid-info"
URL_FM = URL+"first-minute"
URL_faq = URL+"faq"
URL_lm = URL+"last-minute"
URL_stat = URL+"spanelsko"
URL_groupsearch = URL+"vysledky-vyhledavani?tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9|10|11|12|13&ic1=1&ac1=2"
URL_FT_results = URL+"hledani-vysledky?q="
URL_SRL_kuba_regres = URL+"vysledky-vyhledavani?ac1=2&d=63888&dd=2023-07-01&nn=7|8|9|10|11|12|13|14|15|16|17|18|19|20|21&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"



def tearDown(self):
  print(self.driver.current_url)
  self.driver.quit()
  #if not self.test_passed:self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

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
  try:
    generalDriverWaitImplicit(driver)
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
    pass

