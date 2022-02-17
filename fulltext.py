from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, URL
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.fischer.cz/hledani-vysledky?q=zanzibar")

acceptConsent(driver)

vysledkyHlavniGrid = driver.find_elements_by_xpath("//*[@class='grd-col grd-col--9 grd-col--md-12 f_fulltextResults-main']")

print(vysledkyHlavniGrid)
print(vysledkyHlavniGrid[0].get_attribute("href"))


linksToCheckList = []

vysledkyDlazdiceHotelu = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']/a")
x=0
for _ in vysledkyDlazdiceHotelu:

    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
    x=x+1


print(linksToCheckList)