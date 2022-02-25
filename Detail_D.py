from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest


##there is new SRL rn so gotta prepare that, for now I created this test just for the detail of hotel it self, hard url

class TestDetailHotelu_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_detail_isDisplayed(self):
        self.driver.get(URL_detail)
        self.driver.maximize_window()
        time.sleep(5)
        acceptConsent(self.driver)
        wait = WebDriverWait(self.driver, 150000)
        try:
            detailFotka = self.driver.find_element_by_xpath("//*[@id='gallery01Trigger']")
            wait.until(EC.visibility_of(detailFotka))
            print (detailFotka.is_displayed)

            if detailFotka.is_displayed():
                pass
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkami na detailu hotelu " + url
            sendEmail(msg)

        assert detailFotka.is_displayed == True

        try:
            sedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
            wait.until(EC.visibility_of(sedivka))
            if sedivka.is_displayed():
                pass


        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem se sedivkou na detailu hotelu " + url
            sendEmail(msg)

        try:
            terminyCeny = self.driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            self.driver.execute_script("arguments[0].click();", terminyCeny)
            try:
                potvrdit = self.driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
                self.driver.execute_script("arguments[0].click();", potvrdit)

            except NoSuchElementException:
                pass


        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem prepnuti na terminy a ceny na detailu hotelu " + url
            sendEmail(msg)

        try:
            terminySingle = self.driver.find_element_by_xpath("//*[@data-hotel]")
            wait.until(EC.visibility_of(terminySingle))

            terminySingle.is_displayed == True
            if terminySingle.is_displayed():
                pass
            else:
                url = self.driver.current_url
                msg = "Problem s terminy a ceny na detailu hotelu " + url
                sendEmail(msg)


        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s terminy a ceny na detailu hotelu " + url
            sendEmail(msg)

