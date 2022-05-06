import time
from selenium.common.exceptions import NoSuchElementException
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

def generalized_SRL_choose


