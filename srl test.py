import pytest
import time
import json
from to_import_secret import sendEmail
from selenium.webdriver.remote import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from to_import import acceptConsent, closeExponeaBanner


class test_srl2_C:

    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1

        URL_SRL = "https://fischer.web2.dtweb.cz/vysledky-vyhledavani?d=1009|953|1108|592|611|610|612|1010|590|726|609|621|680|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=8&kc1=1&ac1=2"
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150000)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)

        try:
            hotelyAllKarty = self.driver.find_elements_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")

            wait.until(EC.visibility_of(hotelyAllKarty[0]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)

        for WebElement in hotelyAllKarty:

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
            print(cenaZajezduAdultString)

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

            if detailPokojSedivkaString == pokojZajezduString:
                print("pokoje sedi srl vs detail")
            else:
                print(" nesedi pokoj SRL vs sedivka")

            if detailStravaSedivkaString == stravaZajezduString:
                print("stravy sedi srl vs detail")

            else:
                print("nesedi strava srl vs ssedika")

            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")

            else:
                print("ceny all problem srl vs detail")

            if detailCenaAdultString == cenaZajezduAdultString:
                print(" cena adult sedi srl vs detail")

            else:
                print("cena adult nesedi srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            print(x)
            windowHandle = windowHandle + 1
            print(windowHandle)



    def test_SRL_mostExpensive_C(self):
        URL_SRL = "https://fischer.web2.dtweb.cz/vysledky-vyhledavani?d=1009|953|1108|592|611|610|612|1010|590|726|609|621|680|622|669|1086|1194|670|978|594|675|683&tt=1&to=4312|4305|2682|4308&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ka1=8&kc1=1&ac1=2"
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150000)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)

        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []  ##second list takes the values too, then sorts it low to high

        sortByMostExpensive = self.driver.find_element_by_xpath("//*[contains(text(), 'od nejdražšího')]")
        sortByMostExpensive.click()

        hotelyKarty = self.driver.find_element_by_xpath(
            "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
        wait.until(EC.visibility_of(hotelyKarty))
        time.sleep(10)
        x = 0
        cenaZajezduAll = self.driver.find_elements_by_xpath(
            "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

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