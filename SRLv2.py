from to_import import acceptConsent, URL, URL_stat, caps, closePopupBanner, URL_groupsearch
import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from close_exponea_banner import closeExponeaBanner
driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver91.exe")
##URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?d=735|618|619|973|709|595|648|972|746|741|1093|603|620|623|624|993|826&tt=1&dd=2021-09-06&rd=2021-11-06&nn=7|8|9&ac1=2"
URL_SRL = "https://www.eximtours.cz/vysledky-vyhledavani?tt=0&ac1=2&dd=2021-08-27&rd=2021-09-26&nn=7&d=63720|63719&pf=0&pt=900000"


x=0         ##variable for taking the first hotel, starting at 0


driver.get(URL_SRL)
wait = WebDriverWait(driver, 150000)

time.sleep(2)
acceptConsent(driver)
time.sleep(2)
closeExponeaBanner(driver)

terminZajezdu = driver.find_elements_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
terminZajezduSingle = driver.find_element_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

wait.until(EC.visibility_of(terminZajezduSingle))
##print(terminZajezdu[x].text)

linkDetail = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
linkDetailActualUrl = linkDetail[x].get_attribute("href")
##print(linkDetailActualUrl)

stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
stravaZajezduString = stravaZajezdu[x].text

pokojZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
pokojZajezduString = pokojZajezdu[x].text
##print(pokojZajezduString)

cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
cenaZajezduAllString = cenaZajezduAll[x].text
##print(cenaZajezduAllString)

cenaZajezduAdult = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
cenaZajezduAdultString = cenaZajezduAdult[x].text
print(cenaZajezduAdultString)



driver.execute_script("window.open("");")
driver.switch_to.window(driver.window_handles[1])
driver.get(linkDetailActualUrl)

detailTerminSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
##print(detailTerminSedivka.text)

detailStravaSedivka = driver.find_elements_by_xpath("//*[@class='fshr-detail-summary-paragraph']")
detailStravaSedivkaString = detailStravaSedivka[1].text         ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully

detailPokojSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
detailPokojSedivkaString = detailPokojSedivka.text
detailPokojSedivkaString = detailPokojSedivkaString[:-3]            ##need to be edited cuz there is random spaces and "?" in the element
##print(detailPokojSedivkaString)

detailCenaAll = driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
detailCenaAllString = detailCenaAll.text
##print(detailCenaAllString)

detailCenaAdult = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-price-header'] //*[@class='fshr-price']")
detailCenaAdultString = detailCenaAdult.text
print(detailCenaAdultString)


if detailPokojSedivkaString == pokojZajezduString:
    print("pokoje sedí srl vs detail")
else:
    print(" nesedí pokoj SRL vs sedivka")

if detailStravaSedivkaString == stravaZajezduString:
    print("stravy sedí srl vs detail")

else:
    print( "nesedí strava srl vs ssedika")

if detailCenaAllString == cenaZajezduAllString:
    print ("ceny all sedí srl vs detail")

else:
    print("ceny all problem srl vs detail")

if detailCenaAdultString == cenaZajezduAdultString:
    print(" cena adult sedí srl vs detail")

else:
    print("cena adult nesedi srl vs detail")