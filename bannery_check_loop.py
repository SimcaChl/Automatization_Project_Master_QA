import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
URL = "https://www.fischer.cz"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)

