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
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")

URL_detail_exim = "https://www.fischer.cz/recko/kreta-heraklion/bali/athina?DS=1024&GIATA=8225&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=9043&MT=2&RT=22&NN=7&RD=2022-07-14&DD=2022-07-07&DP=2682&MNN=7|8|9&TT=1&PID=5613&DPR=EXIM%20TOURS&TTM=1&DF=2022-07-07|2022-08-07&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
URL_dx = "https://www.fischer.cz/hotely/recko/kreta/sissi/bella-vista-sissi-recko?DS=2&GIATA=1020&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=282531&MT=0&RT=22&NN=7&RD=2022-07-08&DD=2022-07-01&DP=2563&MNN=7|8|9&TT=1&PID=AMTSGR2CHQ&DPR=OTSCKF&TTM=1&DF=2022-07-01|2022-08-01&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
URL_statik = "https://www.fischer.cz/recko/samos/pythagorion/maritsa-bay?DS=1&GIATA=17012&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=65254&MT=2&DI=47&RT=15&NN=7&RD=2022-08-30&DD=2022-08-23&DP=4312&MNN=7|8|9&TT=1&PID=SMMAR&DPR=Fischer&TTM=1&DF=2022-08-23|2022-09-23&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
wait = WebDriverWait(driver, 150000)
driver.get(URL_dx)
def detail_fotka(driver):
    imageDetail = driver.find_element_by_xpath("//*[@id='gallery01Trigger']//img")
    imageDetailSrc = imageDetail.get_attribute("src")
    try:
        driver.set_page_load_timeout(5)
        driver.get(imageDetailSrc)
    except TimeoutException:
        url = driver.current_url
        msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
        sendEmail(msg)

    try:
        image = driver.find_element_by_xpath("/html/body/img")
        if image.is_displayed():
            print("its ok")
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
        sendEmail(msg)

##detail_fotka(driver)

time.sleep(2)
acceptConsent(driver)

time.sleep(1)
closeExponeaBanner(driver)
time.sleep(1)

try:
        terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
        wait.until(EC.visibility_of(terminyCeny))
        terminyCeny.click()
        try:
            potvrdit = driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
            driver.execute_script("arguments[0].click();", potvrdit)

        except NoSuchElementException:
            url = driver.current_url
            msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
            sendEmail(msg)


except NoSuchElementException:
        url = driver.current_url
        msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
        sendEmail(msg)


try:
    stravovaniBox = driver.find_element_by_xpath("//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']")
    wait.until(EC.visibility_of(stravovaniBox))
    stravovaniBox.click()
    try:
        #allInclusiveBox = driver.find_element_by_xpath("//*[contains(text(), 'All inclusive')]")
        #wait.until(EC.visibility_of(allInclusiveBox))
        ##allInclusiveBox.click()
        stravyBox = driver.find_elements_by_xpath("//*[@name='detailFilterCatering']")

        driver.execute_script("arguments[0].click();", stravyBox[1])

        try:
            potvrditButtonBox = driver.find_element_by_xpath("//*[@class='fshr-filter-footer'] //*[contains(text(), 'Potvrdit')]")
            #wait.until(EC.visibility_of(potvrditButtonBox))
            #potvrditButtonBox.click()
            driver.execute_script("arguments[0].click();", potvrditButtonBox)

        except NoSuchElementException:
            url = driver.current_url
            msg = "potvrditButtonBox, potvrzeni stravy na detailu hotelu problém, NoSuchElementException " + url
            sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "allInclusiveBox, zvolení stravy na detailu hotelu problém, NoSuchElementException " + url
        sendEmail(msg)

except NoSuchElementException:
    url = driver.current_url
    msg = "stravovaniBox, otevření filtru stravování detail hotelu, NoSuchElementException " + url
    sendEmail(msg)


