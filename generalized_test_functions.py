import time

#zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"

def generalized_map_test(driver, zobrazitNaMapeXpath):
    def click_on_map_circle(driver, circlexpath):
        try:
            driver.find_element_by_xpath(circlexpath).click()
        except:
            print("nenasel se large kolecko")
            pass
        time.sleep(2.4)

    zobrazitNaMape = driver.find_element_by_xpath(zobrazitNaMapeXpath)
    zobrazitNaMape.click()
    largeCircleXpath = "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"

    time.sleep(15)##loading time
    click_on_map_circle(driver, largeCircleXpath)
    click_on_map_circle(driver, largeCircleXpath)
    click_on_map_circle(driver, largeCircleXpath)




    ##Medium kolecko

    try:
        mediumKolecko = driver.find_elements_by_xpath(
            "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).click()
        # wait.until(EC.element_to_be_clickable((By.XPATH,
        # "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).execute_script("arguments[0].click();", mediumKolecko[1])
    except :
        pass

    ##small kolecko

    try:
        koleckoCisloSmall = driver.find_element_by_xpath(
            "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']")
        koleckoCisloSmall.click()
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-small leaflet-zoom-animated leaflet-interactive']"))).click()
    except NoSuchElementException:
        print("nenasel se small kolecko")
        pass
    except TimeoutException:
        print("nenasel se small kolecko")
        pass
    except ElementNotInteractableException:
        print("nenasel se small kolecko ElementNotInteractableException")
        pass

    time.sleep(3)

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

    time.sleep(5)

    ###EXECUTION DISPLAY TEST NA DETAIL HOTELU -> pokud se vyassertuje že jsem na detailu a vše je ok můžu předpokládat že mapka je OK

    try:
        sedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
        wait.until(EC.visibility_of(sedivka))
        assert sedivka == True


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)

    try:
        terminSedivkaSingle = self.driver.find_element_by_xpath("//*[@data-hotel]")
        wait.until(EC.visibility_of(terminSedivkaSingle))

        assert terminSedivkaSingle.is_displayed() == True

        if terminSedivkaSingle.is_displayed():
            pass
        else:
            url = self.driver.current_url
            msg = "Problem s terminy a ceny na detailu hotelu " + url
            sendEmail(msg)


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s terminSedivkaSingle " + url
        sendEmail(msg)

