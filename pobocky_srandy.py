import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
URL = "https://www.fischer.cz/kontakty/seznam-pobocek"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)



start = "//*[@data-branch-id='248']"
end = "//*[@data-branch-id='493']"
stringToVerify = """Benešov
>
Zavřeno
"""
## https://webadmin-shared.stg.dtweb.cz/OfficeBranchAdmin?fragmentGuid=00000000-0000-0000-0000-000000000000

def id_creator_pobocky_xpath(idNumber):
    startXpath = "//*[@data-branch-id='"
    endXpath = "']"

    finalIdXpathLocator = startXpath + str(idNumber) + endXpath
    return finalIdXpathLocator

print(driver.find_element_by_xpath(id_creator_pobocky_xpath(248)).text)
#print(stringToVerify)
#print(driver.find_element_by_xpath(id_creator_pobocky_xpath(248)).text==stringToVerify)
listJmenaPobocek = []
idCountPobocekStarter = 248
for i in range(245):
#
    print(2)

    idCountPobocekStarter = idCountPobocekStarter+1