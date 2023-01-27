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
pobockaBoxXpath = "//*[@data-branch-id='248']"
pobockaBoxElement = driver.find_element_by_xpath(pobockaBoxXpath)

pobockaBoxElement.click()


