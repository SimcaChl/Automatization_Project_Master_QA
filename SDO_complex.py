from to_import import acceptConsent, URL, URL_stat, caps, URL_groupsearch, closeExponeaBanner
from to_import_secret import sendEmail
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

UR="https://www.eximtours.cz/turecko"

driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
wait = WebDriverWait(driver, 150000)
driver.get(UR)
driver.maximize_window()
time.sleep(2.5)
acceptConsent(driver)
time.sleep(2.5)
closeExponeaBanner(driver)

bigMap = driver.find_element_by_xpath("//*[@class='leaflet-gl-layer mapboxgl-map']")


##wait.until(EC.element_to_be_clickable(koleckoCislo[0]))
#wait.until(EC.visibility_of(koleckoCislo))
time.sleep(5)
#actions = ActionChains(driver)
#actions.move_to_element(bigMap).perform()

time.sleep(2)
try:
    koleckoCislo = driver.find_elements_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']")
    koleckoCislo[0].click()
except ElementClickInterceptedException:
    pass



time.sleep(5)
koleckoCislo[0].click()

actualHotelPin = driver.find_element_by_xpath("//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
    ##actualHotelPin.click()
driver.execute_script("arguments[0].click();", actualHotelPin)

time.sleep(2)

hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
hotelBubble.click()