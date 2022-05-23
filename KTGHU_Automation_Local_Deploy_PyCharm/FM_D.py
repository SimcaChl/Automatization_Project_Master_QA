from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from KTGHU_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown

from KTGHU_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest



class TestFM_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_D(self):
        self.driver.get(URL_FM)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        groupSearch_D(self, self.driver)
        self.test_passed = True