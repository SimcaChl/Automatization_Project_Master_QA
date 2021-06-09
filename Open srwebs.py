from FUNCTIONS import *
from selenium.webdriver.common.keys import Keys
fischer = "https://fischer.web"
exim = "https://exim.web"

def URLsrweb(cisloNodu, web):
    URL = web + cisloNodu + ".dtweb.cz/"
    print(URL)
    return URL



driver.get("https://google.cz")
driver.execute_script("window.open('https://fischer.web1.dtweb.cz/')")
driver.execute_script("window.open('https://fischer.web2.dtweb.cz/')")
driver.execute_script("window.open('https://fischer.web3.dtweb.cz/')")
driver.execute_script("window.open'https://exim.web1.dtweb.cz/'")
driver.execute_script("window.open'https://exim.web2.dtweb.cz/'")
driver.execute_script("window.open'https://exim.web3.dtweb.cz/'")
