from to_import import acceptConsent, URL, URL_stat, caps, URL_groupsearch, closeExponeaBanner
from to_import_secret import sendEmail
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
##sorted by nejlevnejsi
##URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?qf=109_0_50|386_1_0|108_1_0&sortby=PriceTotal&sa=2138|1949|2730&tt=1&to=4312&dd=2021-12-01&rd=2021-12-31&nn=7|8|9&ac1=2&m=5"
##not sorted
URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?d=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&tt=1&dd=2021-10-07&rd=2021-12-07&nn=7|8|9&ac1=2"

def SRL_sort_cheapest():

    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    cenaZajezduAllList = []                     ##one list that takes prices from the srl
    cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high

    sortByCheapest = driver.find_element_by_xpath("//*[contains(text(), 'od nejlevnějšího')]")
    sortByCheapest.click()

    hotelyKarty = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
    wait.until(EC.visibility_of(hotelyKarty))
    time.sleep(10)
    x=0
    cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

    for WebElement in cenaZajezduAll:
        cenaZajezduAllString = cenaZajezduAll[x].text
        cenaZajezduAllString = cenaZajezduAllString[:-3]
        cenaZajezduAllString = ''.join(cenaZajezduAllString.split())        ##delete spaces
        cenaZajezduAllString = int(cenaZajezduAllString)        ##convert to int to do sort easily
        x=x+1
        cenaZajezduAllList.append(cenaZajezduAllString)
        cenaZajezduAllListSorted.append(cenaZajezduAllString)

    cenaZajezduAllListSorted.sort()     ##sorting second list low to high


    if cenaZajezduAllListSorted == cenaZajezduAllList:          ##compare first list to second list, if is equal = good
        print("Razeni od nejlevnejsiho je OK")

    else:
        print("Razeni od nejlevnejsiho je spatne")



    print(cenaZajezduAllList)
    print(cenaZajezduAllListSorted)


def SRL_sort_most_expensive():      ##the same only difference 1)click on nejdrazsi 2) sort list reverse=true
    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    cenaZajezduAllList = []                     ##one list that takes prices from the srl
    cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high

    sortByMostExpensive = driver.find_element_by_xpath("//*[contains(text(), 'od nejdražšího')]")
    sortByMostExpensive.click()

    hotelyKarty = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
    wait.until(EC.visibility_of(hotelyKarty))
    time.sleep(10)
    x=0
    cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

    for WebElement in cenaZajezduAll:
        cenaZajezduAllString = cenaZajezduAll[x].text
        cenaZajezduAllString = cenaZajezduAllString[:-3]
        cenaZajezduAllString = ''.join(cenaZajezduAllString.split())
        cenaZajezduAllString = int(cenaZajezduAllString)
        ##print(type(cenaZajezduAllString))
        x=x+1
        cenaZajezduAllList.append(cenaZajezduAllString)
        cenaZajezduAllListSorted.append(cenaZajezduAllString)


    cenaZajezduAllListSorted.sort(reverse=True)


    if cenaZajezduAllListSorted == cenaZajezduAllList:
        print("Razeni od nejdrazshio je OK")

    else:
        print("Razeni od nejdrazshio je spatne")



    print(cenaZajezduAllList)
    print(cenaZajezduAllListSorted)
##SRL_sort_cheapest()
##SRL_sort_most_expensive()

def SRL_map():
    driver.get(URL_SRL)
    time.sleep(5)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)
    zobrazitNaMape = driver.find_element_by_xpath("//*[@class='f_bar-item f_bar-map']")
    zobrazitNaMape.click()

    time.sleep(5)##try except na kolecko, pokud ok tak click, nenajde tak pokracovat dal
    koleckoCislo = driver.find_element_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
    koleckoCislo.click()
    time.sleep(5)

    actualHotelPin = driver.find_element_by_xpath("//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
    ##actualHotelPin.click()
    driver.execute_script("arguments[0].click();", actualHotelPin)          ##at this point im at detail hotelu na mapě

    try:
        imgMissing = driver.find_element_by_xpath("//*[@class='f_image f_image--missing']")         ##when theres no photo on the detail on map theres actually class that says it is missing
        if imgMissing.is_displayed():                                                               ##so if I dont find this class = good
            hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
            msg = "V mape v bublibně hotelu se nezobrazuje fotka hotelu " + hotelBubble.text
            sendEmail(msg)

    except NoSuchElementException:
        print("actually OK")

    time.sleep(2)

    hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
    hotelBubble.click()
    ##end at detail hotelu
#SRL_map()

def SRL_filtr_strava():     ##jen na allinclusive, muzu si pohrat pozdeji for now enough
    driver.get(URL_SRL)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)
    time.sleep(2)

    stravaMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[contains(text(), 'Strava')]")
    stravaMenu.click()
    time.sleep(1)

    allinclusiveMenu = driver.find_element_by_xpath("//*[@value='5']")          ##papani v menu ma vzdy vlastni value, 5=all inclusive
    allinclusiveMenu.click()

    potvrditMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[@class='f_button f_button--common f_button_set--smallest']")
    potvrditMenu.click()
    time.sleep(2)       ##potvrzeno chvilak casu na relload


    stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
    x=0
    stravaZajezduList = []
    for WebElement in stravaZajezdu:
        stravaZajezduString = stravaZajezdu[x].text
        stravaZajezduList.append(stravaZajezduString)
        x=x+1

    y=0
    for _ in stravaZajezduList:
        if "All inclusive" in stravaZajezduList[y]:
        ##if stravaZajezduList[y] == "All inclusive":
            print("ok")
            y=y+1

        else:
            print("stravy nesedi k filtru")
            y = y + 1
    print(stravaZajezduList)
##SRL_filtr_strava()

