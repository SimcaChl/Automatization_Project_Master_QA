from to_import import acceptConsent, URL, URL_stat, caps, URL_groupsearch, closeExponeaBanner
import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

##driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver91.exe")

def groupsearch_test(driver):
    ##driver.get(URL_groupsearch)
    time.sleep(1.5)
    driver.maximize_window()
    acceptConsent(driver)
    closeExponeaBanner(driver)
    teaserItems = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")

    try:
        for WebElement in teaserItems:
            ##print(len(teaserItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                ##print("Else")
                ##emailfunciton

    except NoSuchElementException:
            pass
            ##print("no such")
            ##email fnction

    srlItems = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]")
    try:
        for WebElement in srlItems:
            ##print(len(srlItems))
            jdouvidet = WebElement.is_displayed()
            ##print(jdouvidet)
            if jdouvidet == True:
                ##print(jdouvidet)
                ##print(WebElement)
                pass

            else:
                pass
                ##print("Else")
                ##emailfunciton


    except NoSuchElementException:
        pass
        ##print("no such")
        ##email fnction


