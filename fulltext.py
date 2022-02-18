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
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.fischer.cz/hledani-vysledky?q=zanzibar")
acceptConsent(driver)
vysledkyHlavniGrid = driver.find_elements_by_xpath("//*[@class='grd-col grd-col--9 grd-col--md-12 f_fulltextResults-main']")
linksToCheckList = []
vysledkyDlazdiceHotelu = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']/a")
x=0
for _ in vysledkyDlazdiceHotelu:

    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
    x=x+1


vysledkyTextItems = driver.find_elements_by_xpath("//*[@class='f_fulltextResults-item']/a")
z=0
for _ in vysledkyTextItems:

    linksToCheckList.append(vysledkyTextItems[0].text)
    z=z+1

print(linksToCheckList)

print(len(linksToCheckList))
responseList = []
y=0
for _ in linksToCheckList:
    response = requests.get(linksToCheckList[y])
    print(response.status_code)
    print(response.status_code==200)
    y=y+1