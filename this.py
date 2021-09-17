import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_stat, caps, closePopupBanner
from SRL_test import test_SRL
from close_exponea_banner import closeExponeaBanner
from group_search import groupsearch_test
from SRLv2 import SRLtestV2

##udelat list ze vsech banneru href a pak na ne volat znova vsechny ty srlv2 testy


driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver92.exe")
wait = WebDriverWait(driver, 150000)
driver.get(URL)
driver.maximize_window()
time.sleep(1.5)
acceptConsent(driver)
time.sleep(2.5)
closeExponeaBanner(driver)



banneryAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']/a")
##print(banneryAll)
##print(len(banneryAll))
x=0
for WebElement in banneryAll:
    bannerHref = banneryAll[x].get_attribute("href")
    ##print(bannerHref)
    x=x+1
    ##print(x)
    driver.execute_script("window.open("");")
    driver.switch_to.window(driver.window_handles[x])
    driver.get(bannerHref)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)


tabsCount = len(driver.window_handles)
driver.current_url
driver.switch_to.window(driver.window_handles[0])


srlURL = URL+"/vysledky-vyhledavani?d="
groupURL = URL+"/vysledky-vyhledavani?tt="
tabsCount = len(driver.window_handles)

banneryOdkazySRL = []
while tabsCount > 0:
    tabsCount = tabsCount - 1       ##
    driver.switch_to.window(driver.window_handles[tabsCount])
    currentURL = driver.current_url
    time.sleep(3)
    ##print(currentURL)
    if srlURL in currentURL:
        print("je to klasik SRL")
        currentURLtrueSRL = driver.current_url
        banneryOdkazySRL.append(currentURLtrueSRL)
        test_SRL(driver)


    if groupURL in currentURL:
        print("je to group search")
        groupsearch_test(driver)

print(banneryOdkazySRL)
tabsCount = len(driver.window_handles)
print(tabsCount)
while tabsCount > 1:
    tabsCount = tabsCount - 1
    driver.switch_to.window(driver.window_handles[tabsCount])
    driver.close()

z=0
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

kolikVasBude = driver.find_element_by_xpath('//*[@class="f_button f_button--filter"]//*[@class="f_button-content f_icon f_icon--crowd"]')
kolikVasBude.click()
pridatPokoj = driver.find_element_by_xpath('//*[@class="f_anchor f_icon f_icon--plus"]')

wait.until(EC.visibility_of(pridatPokoj))
pridatPokoj.click()

potvrditAvyhledat = driver.find_element_by_xpath("//span[contains(text(),'Potvrdit a vyhledat')]")
potvrditAvyhledat.click()

time.sleep(1)
driver.get(URL)
time.sleep(3)

for _ in banneryOdkazySRL:
    time.sleep(4)
    driver.get(banneryOdkazySRL[z])
    SRLtestV2(driver)
    time.sleep(1)
    tabsCount = len(driver.window_handles)
    while tabsCount > 1:
        tabsCount = tabsCount - 1
        driver.switch_to.window(driver.window_handles[tabsCount])
        driver.close()

    driver.switch_to.window(driver.window_handles[0]) ##this has to happen if it doesnt selenium returns error no such window even though there is only one tab active, silly selenium kek
    z=z+1
time.sleep(10)

