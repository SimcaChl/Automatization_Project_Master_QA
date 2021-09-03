import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_stat, caps, closePopupBanner
from SRL_test import test_SRL
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver92.exe")
wait = WebDriverWait(driver, 150000)
URL = "https://www.fischer.cz/first-minute "
driver.get(URL)
acceptConsent(driver)
time.sleep(3)

##banner = driver.find_elements_by_xpath("//*[@class='f_teaser-item']//*[@class='f_tile f_tile--teaserDestination']")
banner2 = driver.find_element_by_xpath("//*[@class='f_teaser-item']/a")
banner3 = driver.find_element_by_xpath("/html/body/section[9]/div/div/div/div/div/div/div/div/div[11]/a")
print(banner3)
print (banner3.value_of_css_property(banner3))
print(banner3.get_property('style'))
print(banner2.get_property('style'))

time.sleep(12)