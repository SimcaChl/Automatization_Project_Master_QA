from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, URL
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest



class TestFulltext(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_fulltext_naseptavac(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        FTlupa = self.driver.find_element_by_xpath("//*[@class='f_anchor f_icon f_icon--magnifier']")
        FTlupa.click()
        query = "Zanzibar"
        inputBox = self.driver.find_element_by_xpath("//*[@class='f_input-item j_input']")
        inputBox.send_keys(query)
        time.sleep(1)
        # inputBox.send_keys(Keys.ENTER)
        prvniItem = self.driver.find_elements_by_xpath("//*[@class='f_item']")
        prvniItem[0].click()

        currentUrl = self.driver.current_url
        assert currentUrl != URL
