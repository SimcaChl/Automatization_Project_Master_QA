from selenium.webdriver.chrome import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_groupsearch, setUp, tearDown
import unittest
from to_import import URL
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get(URL)

time.sleep(5)
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


