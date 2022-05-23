from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from to_import_master import sendEmail


def generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath):
    def click_on_map_circle(driver, circlexpath):
        try:
            driver.find_element_by_xpath(circlexpath).click()
        except:
            print("nenasel se kolecko" +circlexpath)
            pass
        time.sleep(1.2)

    zobrazitNaMape = driver.find_element_by_xpath(zobrazitNaMapeXpath)
    zobrazitNaMape.click()
    largeCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"
    mediumCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"
    smallCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']"
    time.sleep(10)##loading time
    click_on_map_circle(driver, largeCircleXpath)
    click_on_map_circle(driver, largeCircleXpath)
    click_on_map_circle(driver, largeCircleXpath)

    click_on_map_circle(driver, mediumCircleXpath)
    click_on_map_circle(driver, mediumCircleXpath)

    click_on_map_circle(driver, smallCircleXpath)
    click_on_map_circle(driver, smallCircleXpath)

def generalized_map_test_click_on_pin_and_hotel_bubble(driver):
    actualHotelPin = driver.find_element_by_xpath(
        "//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
    driver.execute_script("arguments[0].click();", actualHotelPin)  ##at this point im at detail hotelu na mapě

    try:
        imgMissing = driver.find_element_by_xpath(
            "//*[@class='f_image f_image--missing']")  ##when theres no photo on the detail on map theres actually class that says it is missing
        if imgMissing.is_displayed():  ##so if I dont find this class = good
            hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
            msg = "V mape v bublibně hotelu se nezobrazuje fotka hotelu " + hotelBubble.text
            sendEmail(msg)

    except NoSuchElementException:
        print("actually OK")

    time.sleep(2)

    hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
    hotelBubble.click()

def generalized_SRL_choose_meal_filter_EW_like(driver, stravaMenuXpath):
    stravaMenu = driver.find_element_by_xpath(stravaMenuXpath)
    stravaMenu.click()
    time.sleep(2)

def generalized_SRL_choose_meal_filter_FW_like(driver, stravaMenuXpath, stravaMenuAllInclusiveXpath, potvrditMenuXpath):
    #stravaMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[contains(text(), 'Strava')]")
    stravaMenuBox = driver.find_element_by_xpath(stravaMenuXpath)

    stravaMenuBox.click()
    generalized_SRL_choose_meal_filter_EW_like(driver, stravaMenuAllInclusiveXpath)

    potvrditMenu = driver.find_element_by_xpath(potvrditMenuXpath)
    potvrditMenu.click()

##variable_to_assert_to == .lower should be on default
def generalized_list_string_sorter(driver, web_elements_Xpath, variable_to_assert_to):
    time.sleep(2)
    web_elements = driver.find_elements_by_xpath(web_elements_Xpath)

    list_web_elements_Position = 0
    list_web_elements = []

    for _ in web_elements:
        list_web_elements_String = web_elements[list_web_elements_Position].text.lower()
        list_web_elements.append(list_web_elements_String)

        list_web_elements_Position = list_web_elements_Position + 1

    list_web_elements_Position = 0

    for _ in list_web_elements:
        assert variable_to_assert_to in list_web_elements[list_web_elements_Position]
        if variable_to_assert_to in list_web_elements[list_web_elements_Position]:
            print("ok")
            list_web_elements_Position = list_web_elements_Position + 1

        else:
            print("stravy nesedi k filtru")
            list_web_elements_Position = list_web_elements_Position + 1

    print(list_web_elements)

#predisposition:
#loaded SRL -> clicks on sorter (expensive VS cheap)
#gets all prices

##typeOfSort = cheap or expensive
def generalized_SRL_price_sorter(driver, sorter_Xpath, hotelyKartyXpath, cenaZajezduXpath,  typeOfSort):
        wait = WebDriverWait(driver, 25)

        cenaZajezduAllList = []                     ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high
        time.sleep(2)
        sorter_Element = driver.find_element_by_xpath(sorter_Xpath)
        wait.until(EC.visibility_of(sorter_Element))
        sorter_Element.click()

        hotelyKarty = driver.find_element_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyKarty))
        time.sleep(4)
        list_web_elements_Position = 0
        cenaZajezduAll = driver.find_elements_by_xpath(cenaZajezduXpath)
        wait.until(EC.visibility_of(cenaZajezduAll[0]))

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[list_web_elements_Position].text
            cenaZajezduAllString = cenaZajezduAllString[:-3]
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())        ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)        ##convert to int to do sort easily
            list_web_elements_Position = list_web_elements_Position + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)


        if typeOfSort == "cheap":
            cenaZajezduAllListSorted.sort()  ##sorting second list low to high

            if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
                print("Razeni od nejlevnejsiho je OK")

            else:
                print("Razeni od nejlevnejsiho je spatne")

        if typeOfSort == "expensive":
            cenaZajezduAllListSorted.sort(reverse=True)

            if cenaZajezduAllListSorted == cenaZajezduAllList:
                print("Razeni expensive je OK")

            else:
                print("Razeni expensive je OK")


        print(cenaZajezduAllList)
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList