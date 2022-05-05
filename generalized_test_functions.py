import time

#zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"

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





