import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, caps, closeExponeaBanner


def proklikNaSRLzHP(driver):

    driver.get(URL)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    time.sleep(2.5)
    acceptConsent(driver)

    try:
        lmZajezdNej = driver.find_element_by_xpath(
            "//*[@class='fshr-lm-table-item-content']")
        wait.until(EC.visibility_of(lmZajezdNej))
        ##lmZajezdNej.click()
        driver.execute_script("arguments[0].click();", lmZajezdNej)  ####.click nefunguje na fischer NNN LM/FM, chrome
    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem HP-Nej. nabidka - nenasel se LM zajezd" + url
        sendEmail(msg)

    time.sleep(2)
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
def SRL_test(driver):

    ##driver = webdriver.Remote(
        ##command_executor=comandExecutor,
       ## desired_capabilities=desired_cap)

    driver.get("https://www.eximtours.cz/vysledky-vyhledavani?d=64419|64420|64425&tt=1&dd=2021-10-15&rd=2021-12-15&nn=7|8|9&ka1=9&kc1=1&ac1=2")
    wait = WebDriverWait(driver, 150000)
    ##proklikNaSRLzHP(driver)

    try:
        hotelySingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")        ##
        hotelyAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
        wait.until(EC.visibility_of(hotelySingle))
        ##print(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    pass
                    ##print("hotely jdou videt")

                else:
                    url = driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " +url
                    sendEmail(msg)
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)


    try:
        fotkyAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")         ##
        fotkaSingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")
        wait.until(EC.visibility_of(fotkaSingle))
        ##print(fotkaSingle)
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    pass
                    ##print("fotky jdou videt")
                else:
                    url = driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg)


    try:
        cenaAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")     ##
        cenaSingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                    ##print("ceny jdou videt")
                else:
                    url = driver.current_url
                    msg = " Problem s cenami hotelu v searchi " +url
                    sendEmail(msg)


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)


    ##driver.quit()

SRL_test(driver)