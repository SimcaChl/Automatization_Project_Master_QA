import time

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

from webdriver_manager.chrome import ChromeDriverManager

from ET_Automation_Local_Deploy_PyCharm.to_import_secret import emailPass
from selenium import webdriver
from ET_Automation_Local_Deploy_PyCharm.to_import_secret import comandExecutor



def tearDown(self):
  self.driver.quit()
  if not self.test_passed:
    self.driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "general error"}}')

brand_name_project = "ETRAVEL"
desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name_project,
"build" : "Optimized - Web Monitor V2.1",
"name" : "Faster tests",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"

}
def setUp(self):
 # self.driver = webdriver.Remote(command_executor=comandExecutor,desired_capabilities=desired_cap)
  self.driver = webdriver.Chrome(ChromeDriverManager().install())
  self.test_passed = False


URL = "https://www.etravel.cz/"
#URL = "https://etravel.web3.dtweb.cz/"
#URL = "https://billa.stg.dtweb.cz/"
URL_FM = URL+"first-minute"
URL_exotika = URL + "exoticka-dovolena"
URL_LM = URL+"last-minute"
#URL_SRL = URL+"vysledky-vyhledavani?d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|63219|63341|63428&tt=0&to=4305|4309|2682|4308|4312&dd=2022-09-01&rd=2022-09-25&nn=7|8|9&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL+"vysledky-vyhledavani?d=64419|64420|64425|64423&tt=0&to=4305|4309|2682|4308|4312&dd=2022-09-01&rd=2022-09-25&nn=7|8|9&ka1=5&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63213|63241|63360|63267|74459|74460|63284|74464|63350|63354|74465|63216|63226|63242|63244|74462|63313|74461|74463|63349|63455&tt=0&to=4305|4309|2682|4308|4312&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=6&kc1=1&ac1=2"
#URL_SRL = URL + "vysledky-vyhledavani?d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|64419|64420|64425|64422|64423|63219|63341|63428|63472&tt=1&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=7&kc1=1&ac1=2"
#URL_SRL = "https://www.etravel.cz/vysledky-vyhledavani?d=64419&tt=0&to=4312&dd=2022-06-30&rd=2022-07-08&nn=7|8|9&ac1=2"
#URL_SRL = "https://www.etravel.cz/vysledky-vyhledavani?d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|64419|63252|63447|63232|63247|63249|63250|63251|63280|63289|63528|63325|63326|77802|63527|63345|63361|63381|63526|63401|63450|77804|63461|63470|63219|63341|63428|63472&tt=0&to=4312&dd=2022-06-30&rd=2022-07-08&nn=7|8|9&ka1=7&kc1=1&ac1=2"
#URL_SRL = "https://billa.dev.dtweb.cz/vysledky-vyhledavani?d=63213|63216|63218|63349|63226|63227|63231|64429|63241|63242|63243|63244|63245|74462|63263|63267|74459|63272|74460|63284|63299|63334|63313|74461|78291|74463|63328|74464|63350|64430|63354|63360|63363|74465|63455&tt=1&dd=2022-06-15&rd=2022-06-23&nn=7&ac1=2"
URL_SRL = URL + "vysledky-vyhledavani?d=63448|63260|63213|63241|63360|63267|74459|74460|63284|74464|63350|63354|74465|63216|63226|63242|63244|74462|63313|74461|74463|63349|63455|63288|64154|64152|64153|64157&tt=0&dd=2022-08-12&rd=2022-09-30&nn=7|8|9&ac1=2"
URL_SRL_all_inclusive = URL_SRL + "&m=5"

URL_detail = URL + "egypt/hurghada/hurghada/mirage-bay-resort-a-aqua-park-hurghada?KEY=2257927099&DS=1024&GIATA=16351&D=64419|64420|64425|64422|64423&HID=5057&MT=5&RT=15&NN=7&DF=2022-07-13|2022-09-12&RD=2022-08-15&DD=2022-08-08&AC1=2&KC1=1&KA1=4&IC1=0&DP=4308&MNN=7&NNM=7|8|9&TT=1&TTM=0&PID=33040&DPR=EXIM%20TOURS"
#URL_detail = URL+"recko/lefkada/nidri/delfini-penzion?ds=1024&giata=538958&hid=141090&nn=7&df=2022-07-01|2022-09-01&rd=2022-09-01&dd=2022-08-25&ac1=2&kc1=1&ka1=5&tt=1&pid=335821&d=63220|63281|63373|63442|63311|63314|63316|63319|63324|63333|63390|63402|63408|63409|63471|63219|63341|63428&mt=2&rt=15&dp=4305&mnn=7&nnm=7|8|9&ttm=1&dpr=EXIM%20TOURS&sortby=Price&sortorder=0"
URL_detail_all_inclusive = URL_detail + "&mmt=5"
URL_detail_airport_praha = URL_detail + "&tom=4312"
URL_FT_results = URL + "hledani-vysledky?q="
URL_groupsearch = URL + "vysledky-vyhledavani?tt=1&dd=2022-08-04&rd=2022-09-30&nn=7|8|9&ka1=5&kc1=1&ac1=2"
URL_SDO = URL + "turecko"





def generalDriverWaitImplicit(driver):
  time.sleep(3)
  driver.implicitly_wait(25)
def acceptConsent(driver):
  driver.maximize_window()
  generalDriverWaitImplicit(driver)
  generalDriverWaitImplicit(driver)
  # time.sleep(5)
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
"x"
def returnLocatorForMealHotelKarty(poziceHotelu):
    #string1 = '//*[@id="app"]/pagemainsearchfilter/div/div[4]/div[2]/div/div['
    string1 = "/html/body/div[1]/div/div[4]/div[2]/div/div["
    stringVariable = poziceHotelu
    stringVariable = str(stringVariable)
    string2 = "]/a/div[3]/div[3]/div[2]/span[1]"
    #string2 = ']/a/div[3]/div[3]/div[2]/span[1]'
    finalString = string1 + stringVariable + string2
    finalString = finalString.replace(" ", "")
    #print(finalString)
    return str(finalString)

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

def closeExponeaBanner():
    pass