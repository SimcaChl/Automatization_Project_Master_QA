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


driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver92.exe")
wait = WebDriverWait(driver, 150000)
driver.get(URL)
driver.maximize_window()
time.sleep(1.5)
acceptConsent(driver)
time.sleep(2.5)
closePopupBanner(driver)

##bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
##urlbaneru = bannerSingle.get_attribute("href")


banneryAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']/a")
print(banneryAll)
print(len(banneryAll))
x=0
##bannerLink = driver.find_element_by_xpath('//*[@class="f_teaser-item"]/a')
for WebElement in banneryAll:
    bannerHref = banneryAll[x].get_attribute("href")
    print(bannerHref)
    x=x+1
    print(x)
    driver.execute_script("window.open("");")
    driver.switch_to.window(driver.window_handles[x])
    driver.get(bannerHref)

    driver.switch_to.window(driver.window_handles[0])
    ##time.sleep(3)

##driver.execute_script("window.open('');")

##for _ in banneryAll:
  ##  bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
    ##driver.execute_script("window.open(bannerSingle);")


