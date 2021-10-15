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



URL_no_work = "https://img.fischer.cz/hotels/recko/kreta/plakias/apollo/1162139.jpeg"
URL_work = "https://cdn.fischer.cz/Images/000409/turecko-turecka-riviera-konakli-eftalia-aqua-resort-0_706x424.jpg"

driver.get("https://www.fischer.cz/turecko/turecka-riviera/side/primasol-hane-family?DS=1024&GIATA=40038&D=627|974|596|712|684|955&HID=8554&MT=5&MMT=5&RT=15&NN=7&RD=2021-11-13&DD=2021-11-06&DP=4312&TO=4305|4309|2682|4308|4312&MNN=7|8|9&TT=1&PID=28963&DPR=EXIM%20TOURS&TTM=1&TOM=4305|4309|2682|4308|4312&DF=2021-11-06|2021-12-07&ERM=0&NNM=7|8|9&ac1=2&kc1=1&ka1=10&ic1=0#/fotky")

imageDetail = driver.find_element_by_xpath("//*[@id='gallery01Trigger']//img")
imageDetailSrc = imageDetail.get_attribute("src")

print(imageDetailSrc)

try:
    driver.set_page_load_timeout(5)
    driver.get(imageDetailSrc)
except TimeoutException:
        print("not good")



try:
    image = driver.find_element_by_xpath("/html/body/img")
    if image.is_displayed():
        print("its ok")

except NoSuchElementException:
    print("no such element ex")