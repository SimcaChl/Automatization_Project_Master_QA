from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent
URL_prod_public = "https://www.fischer.cz/"

URL_deploying_web = ""
SRL_H1textPocetNalezenychZajezduXpath = "//h1"


driver = webdriver.Chrome(ChromeDriverManager().install())
URL_deploying_web
def banner_check_public_prod_VS_deployed_web(driver, URL_prod_public ):
    driver.maximize_window()
    driver.get(URL_prod_public)
    time.sleep(2)
    acceptConsent(driver)

    banneryAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']/a")
    x=0
    pocetNalezenychZajezduElementList_PROD = []

    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        print(bannerHref)
        x=x+1
        print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        try:
            pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_PROD.append(pocetNalezenychZajezduElement_PROD)
            print (pocetNalezenychZajezduElement_PROD)
        except NoSuchElementException:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    print(pocetNalezenychZajezduElementList_PROD)

banner_check_public_prod_VS_deployed_web(driver, URL_prod_public )