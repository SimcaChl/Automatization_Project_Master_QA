from to_import import acceptConsent, URL, URL_stat, caps, URL_groupsearch, closeExponeaBanner
from to_import_secret import sendEmail
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?qf=109_0_50|386_1_0|108_1_0&sortby=PriceTotal&sa=2138|1949|2730&tt=1&to=4312&dd=2021-12-01&rd=2021-12-31&nn=7|8|9&ac1=2&m=5"

driver.get(URL_SRL)
wait = WebDriverWait(driver, 150000)

time.sleep(2)
acceptConsent(driver)
time.sleep(2)
closeExponeaBanner(driver)