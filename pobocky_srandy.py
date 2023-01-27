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

brnoAnchorOblibeneVolbyXpath = "//*[@class='f_anchor'and contains(text(), 'Brno')]"
brnoAnchorOblibeneVolbyElement = driver.find_element_by_xpath(brnoAnchorOblibeneVolbyXpath)
brnoAnchorOblibeneVolbyElement.click()

time.sleep(2)

pobockaBoxXpath = "//*[@data-branch-id='262']"
pobockaBoxElement = driver.find_element_by_xpath(pobockaBoxXpath)
pobockaBoxElement.click()

detailPobockyXpath = pobockaBoxXpath + "//*[contains(text(), 'Detail pobočky')]"
detailPobockyElement = driver.find_element_by_xpath(detailPobockyXpath)
driver.execute_script("arguments[0].scrollIntoView();", detailPobockyElement)
detailPobockyElement.click()




popUpObjednavkaNavstevyXpath = "//*[@class='fshr-popupWindow fshr-popupWindow--centered js-form js-popupWindow fshr-icon fshr-icon--man js-sendByAjax js-gtm-trackGoal']"
popUpObjednavkaNavstevyElement = driver.find_element_by_xpath(popUpObjednavkaNavstevyXpath)
print(popUpObjednavkaNavstevyElement.is_displayed())
