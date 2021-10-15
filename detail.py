import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, caps, closeExponeaBanner
from selenium.common.exceptions import NoSuchElementException
import requests
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")





driver.get("https://www.fischer.cz/spanelsko/tenerife/playa-la-arena/bahia-flamingo?DS=1&GIATA=6881&D=953|1108|592|611|610|612|590|726|609|621|1009|680|622|669|1086|1194|670|978|594|675|1010|683&HID=114154&MT=2&DI=47&RT=15&NN=7&RD=2021-11-08&DD=2021-11-01&DP=4312&MNN=7|8|9&TT=1&PID=TBAH&DPR=Fischer&TTM=1&DF=2021-11-01|2021-12-02&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0")

imageDetail = driver.find_element_by_xpath("//*[@id='gallery01Trigger']//img")
imageDetailSrc = imageDetail.get_attribute("src")

print(imageDetailSrc)

try:
    driver.set_page_load_timeout(5)
    driver.get(imageDetailSrc)
except TimeoutException:
    url = driver.current_url
    msg = "Problem s fotkou src, TimeoutException " + url
    sendEmail(msg)

try:
    image = driver.find_element_by_xpath("/html/body/img")
    if image.is_displayed():
        print("its ok")
except NoSuchElementException:
    url = driver.current_url
    msg = "Problem s fotkou src, NoSuchElementException " + url
    sendEmail(msg)