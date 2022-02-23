from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_fmExotika, sendEmail
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest



class TestFMexotika_D(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_FM_exotika_D(self):
        self.driver.get(URL_fmExotika)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)
        try:
            zajezdyFMsingle = self.driver.find_element_by_xpath("//*[@class='page-tour']")
            zajezdyFMall = self.driver.find_elements_by_xpath("//*[@class='page-tour']")
            wait.until(EC.visibility_of(zajezdyFMsingle))
            if zajezdyFMsingle.is_displayed():
                for WebElement in zajezdyFMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem s FM - zajezdy se neukazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s FM - zajezdy se neukazuji " + url
            sendEmail(msg)

        try:
            rozbal = self.driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            wait.until(EC.visibility_of(rozbal))
            self.driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(2)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Nepodarilo se rozbalit FM zajezd " + url
            sendEmail(msg)

        try:
            rozbalenyZajezd = self.driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
            rozbalenyZajezdAll = self.driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
            wait.until(EC.visibility_of(rozbalenyZajezd))
            if rozbalenyZajezd.is_displayed():
                for WebElement in rozbalenyZajezdAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
            sendEmail(msg)

        