from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Test_SRL_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_SRL_sort_cheapest(self):

        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150000)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)

        cenaZajezduAllList = []                     ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high
        time.sleep(2)
        sortByCheapest = self.driver.find_element_by_xpath("//*[contains(text(), 'od nejlevnějšího')]")
        wait.until(EC.visibility_of(sortByCheapest))
        sortByCheapest.click()

        hotelyKarty = self.driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
        wait.until(EC.visibility_of(hotelyKarty))
        time.sleep(10)
        x=0
        cenaZajezduAll = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
        wait.until(EC.visibility_of(cenaZajezduAll[0]))

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

        assert cenaZajezduAllListSorted == cenaZajezduAllList

    def test_SRL_sort_expensive(self):
        driver = self.driver
        driver.get(URL_SRL)
        wait = WebDriverWait(driver, 150000)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)
        closeExponeaBanner(driver)

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high

        sortByMostExpensive = driver.find_element_by_xpath("//*[contains(text(), 'od nejdražšího')]")
        sortByMostExpensive.click()

        hotelyKarty = driver.find_element_by_xpath(
            "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
        wait.until(EC.visibility_of(hotelyKarty))
        time.sleep(10)
        x = 0
        cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[x].text
            cenaZajezduAllString = cenaZajezduAllString[:-3]
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())
            cenaZajezduAllString = int(cenaZajezduAllString)
            ##print(type(cenaZajezduAllString))
            x = x + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort(reverse=True)

        if cenaZajezduAllListSorted == cenaZajezduAllList:
            print("Razeni od nejdrazshio je OK")

        else:
            print("Razeni od nejdrazshio je spatne")

        print(cenaZajezduAllList)
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList

    def test_SRL_map(self):
        driver = self.driver
        driver.get(URL_SRL)
        wait = WebDriverWait(driver, 15)
        time.sleep(5)
        acceptConsent(driver)
        time.sleep(2)
        closeExponeaBanner(driver)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMape = driver.find_element_by_xpath("//*[@class='f_bar-item f_bar-map']")
        zobrazitNaMape.click()

        time.sleep(7)  ##try except na kolecko, pokud ok tak click, nenajde tak pokracovat dal
        ##kolecka jsou definovany podle velikosti - small, medium, large; vzdy se meni v class name

        ##2x vyvolani na large kolecko (jsou destinace kde se musim kliknout na large vickrat
        ##ve vsech except je pass aby to nespadlo kdyby se large nenasel, goal toho testu je se pres mapu proklikat na detail hotelu
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"))).click()

        except NoSuchElementException:
            print("nenasel se large kolecko")
            pass
        except TimeoutException:
            print("nenasel se large kolecko")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
            pass

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-large leaflet-zoom-animated leaflet-interactive']"))).click()

        except NoSuchElementException:
            print("nenasel se large kolecko")
            pass
        except TimeoutException:
            print("nenasel se large kolecko")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
            pass

        ##Medium kolecko

        try:
            mediumKolecko = driver.find_elements_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).click()
            #wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  # "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']"))).execute_script("arguments[0].click();", mediumKolecko[1])
        except NoSuchElementException:
            print("nenasel se medium kolecko-NoSuchElementException")
            pass
        except TimeoutException:
            print("nenasel se medium kolecko - TimeoutExceptio")
            pass
        except ElementNotInteractableException:
            print("nenasel se medium kolecko ElementNotInteractableException")
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

    def test_SRL_filtr_strava(self):
        driver = self.driver
        driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)
        closeExponeaBanner(driver)
        time.sleep(2)

        stravaMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[contains(text(), 'Strava')]")
        stravaMenu.click()
        time.sleep(2)

        generalDriverWaitImplicit(driver)
        allinclusiveMenu = driver.find_element_by_xpath(
            "//*[@class='f_menu-item-content f_menu-item-content--sub'] //*[@class='f_input-label'] //*[contains(text(), 'All inclusive')]")  ##papani v menu ma vzdy vlastni value, 5=all inclusive
        allinclusiveMenu.click()

        potvrditMenu = driver.find_element_by_xpath(
            "//*[@class='f_menu-item']//*[@class='f_button f_button--common f_button_set--smallest']")
        potvrditMenu.click()
        time.sleep(2)  ##potvrzeno chvilak casu na relload

        stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
        x = 0
        stravaZajezduList = []
        for WebElement in stravaZajezdu:
            stravaZajezduString = stravaZajezdu[x].text
            stravaZajezduList.append(stravaZajezduString)
            x = x + 1

        y = 0
        stringInclusve = "All inclusive"
        for _ in stravaZajezduList:
            ##if stravaZajezduList[y] == "All inclusive":
            assert "All inclusive" in stravaZajezduList[y]
            if "All inclusive" in stravaZajezduList[y]:
                print("ok")
                y = y + 1

            else:
                print("stravy nesedi k filtru")
                y = y + 1
        print(stravaZajezduList)
        driver.quit()

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1

        #URL_SRL = "https://fischer.web2.dtweb.cz/vysledky-vyhledavani?d=1009|953|1108|592|611|610|612|1010|590|726|609|621|680|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=8&kc1=1&ac1=2"
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150000)
        wait = WebDriverWait(self.driver, 15)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")

            wait.until(EC.visibility_of(hotelyAllKarty[1]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        for WebElement in hotelyAllKarty:

            print("|||||HOTEL CISLO|||||||" )
            print(x+1)
            print(x + 1)
            print(x + 1)
            terminZajezdu = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
            terminZajezduSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

            wait.until(EC.visibility_of(terminZajezduSingle))
            ##print(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            ##print(linkDetailActualUrl)

            stravaZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
            stravaZajezduString = stravaZajezdu[x].text

            pokojZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
            pokojZajezduString = pokojZajezdu[x].text
            ##print(pokojZajezduString)

            cenaZajezduAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
            cenaZajezduAllString = cenaZajezduAll[x].text
            ##print(cenaZajezduAllString)

            cenaZajezduAdult = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
            cenaZajezduAdultString = cenaZajezduAdult[x].text
            #print(cenaZajezduAdultString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[windowHandle])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(1)  ##natvrdo aby se to neposralo

            detailTerminSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
            ##print(detailTerminSedivka.text)

            detailStravaSedivka = self.driver.find_elements_by_xpath("//*[@class='fshr-detail-summary-paragraph']")
            detailStravaSedivkaString = detailStravaSedivka[
                1].text  ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully

            detailPokojSedivka = self.driver.find_element_by_xpath(
                "//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
            detailPokojSedivkaString = detailPokojSedivka.text
            detailPokojSedivkaString = detailPokojSedivkaString[
                                       :-3]  ##need to be edited cuz there is random spaces and "?" in the element
            ##print(detailPokojSedivkaString)

            detailCenaAll = self.driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
            detailCenaAllString = detailCenaAll.text
            ##print(detailCenaAllString)
            try:
                detailCenaAdult = self.driver.find_element_by_xpath(
                    '//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
                detailCenaAdultString = detailCenaAdult.text
                print(detailCenaAdultString)

            except NoSuchElementException:
                pass
            assert detailPokojSedivkaString == pokojZajezduString

            if detailPokojSedivkaString == pokojZajezduString:
                print("pokoje sedi srl vs detail")
            else:
                print(" NESEDÍ pokoj SRL vs sedivka")

            assert detailStravaSedivkaString == stravaZajezduString
            if detailStravaSedivkaString == stravaZajezduString:
                print("stravy sedi srl vs detail")

            else:
                print("NESEDÍ strava srl vs ssedika")
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")

            else:
                print("ceny all NESEDÍ srl vs detail")

            assert detailCenaAdultString == cenaZajezduAdultString

            if detailCenaAdultString == cenaZajezduAdultString:
                print(" cena adult sedi srl vs detail")

            else:
                print("cena adult NESEDÍ srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            print(x)
            windowHandle = windowHandle + 1
            print(windowHandle)
