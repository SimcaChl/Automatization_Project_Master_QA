from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from FUNCTIONS import *
##URL = "https://exim.web3.dtweb.cz"
URL = "https://www.fischer.cz"
URL_lm = URL+"/last-minute"
URL_fm = URL+"/first-minute"
URL_stat = URL+"/recko"
##driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver90.exe")
##driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver89.exe") ##office location
wait = WebDriverWait(driver, 150000)

##driverChrome = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium Setup\chromedriver89.exe")
##driverIE = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")

##driver_list = [driverIE, driverChrome]