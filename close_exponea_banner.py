from to_import import acceptConsent, URL, URL_stat, caps, closePopupBanner
import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
        exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
        if exponeaBanner.is_displayed():

            wait.until(EC.visibility_of(exponeaBanner))
            exponeaCrossAndBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
            exponeaCrossAndBanner.click()
            time.sleep(2)

    except NoSuchElementException:
        print( "nenasle se exponea banner")
