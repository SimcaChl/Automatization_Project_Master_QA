from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_covidInfo, sendEmail, URL, URL_faq, URL_lm, URL_stat, URL_SRL
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSRL_D(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_SRL_D(self):
        wait = WebDriverWait(self.driver, 150000)
        self.driver.get(URL_SRL)
        acceptConsent(self.driver)

        try:
            hotelySingle = self.driver.find_element_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")  ##
            hotelyAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
            wait.until(EC.visibility_of(hotelySingle))
            ##print(hotelyAll)
            if hotelySingle.is_displayed():
                for WebElement in hotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    print(jdouvidet)
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = " Problem s hotely v searchi - hotelCard " + url
                        sendEmail(msg)
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s hotely v searchi - hotelCard " + url
            sendEmail(msg)

        try:
            fotkyAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")  ##
            fotkaSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")
            wait.until(EC.visibility_of(fotkaSingle))
            ##print(fotkaSingle)
            if fotkaSingle.is_displayed():
                for WebElement in fotkyAll:
                    jdouvidet = WebElement.is_displayed()
                    print(jdouvidet)
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = " Problem s fotkami hotelu v searchi " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem s fotkami hotelu v searchi " + url
            sendEmail(msg)

        try:
            loadingImgSingle = self.driver.find_element_by_xpath(
                "//*[@class='splide__spinner']")  ##loading classa obrazku, jestli tam je = not gud
            if loadingImgSingle.is_displayed():
                url = self.driver.current_url
                msg = " Problem s načítáná fotek v SRL  //*[@class='splide__spinner']" + url
                sendEmail(msg)
        except NoSuchElementException:
            pass

        try:
            cenaAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")  ##
            cenaSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")
            wait.until(EC.visibility_of(cenaSingle))
            if cenaSingle.is_displayed():
                for WebElement in cenaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        print("ceny")
                        pass

                    else:
                        url = self.driver.current_url
                        msg = " Problem s cenami hotelu v searchi " + url
                        sendEmail(msg)


        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s cenami hotelu v searchi " + url
            sendEmail(msg)