from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent
import unittest
URL_prod_public = "https://www.fischer.cz/"

URL_deploying_web = "https://www.fischer.cz/"
SRL_H1textPocetNalezenychZajezduXpath = "//h1"


driver = webdriver.Chrome(ChromeDriverManager().install())
def banner_check_public_prod_VS_deployed_web(driver, URL_prod_public, URL_deploying_web):
    driver.maximize_window()
    driver.get(URL_prod_public)
    time.sleep(2)
    acceptConsent(driver)

    banneryAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']/a")

    x=0
    pocetNalezenychZajezduElementList_PROD = []
    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        #print(bannerHref)
        x=x+1
        #print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        try:
            pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_PROD.append(pocetNalezenychZajezduElement_PROD)
            #print (pocetNalezenychZajezduElement_PROD)
        except NoSuchElementException:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)



    driver.get(URL_deploying_web)
    time.sleep(5)
    x = 0
    pocetNalezenychZajezduElementList_DEPLOY = []
    banneryAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']/a")
    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        #print(bannerHref)
        x = x + 1
        #print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        try:
            pocetNalezenychZajezduElement_DEPLOY = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_DEPLOY.append(pocetNalezenychZajezduElement_DEPLOY)
            #print(pocetNalezenychZajezduElement_DEPLOY)
        except NoSuchElementException:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)


    print("LIST FROM PUBLIC WWW PRODUCTION ")
    print( pocetNalezenychZajezduElementList_PROD)
    print("------------------------------------------")
    print("LIST FROM DEPLOYING WEB ")
    print(pocetNalezenychZajezduElementList_DEPLOY)

    assert pocetNalezenychZajezduElementList_DEPLOY == pocetNalezenychZajezduElementList_PROD


banner_check_public_prod_VS_deployed_web(driver, URL_prod_public, URL_deploying_web)