from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown, URL
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from ET_Automation_Local_Deploy_PyCharm.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D, imgHotelKartaXpath, destinationXpath, gridDestinationXpath

hlavickaMenuXpath = "//*[@class='inner']"
zlutakHPXpath = "//*[@id='c_mainSearchFilter']"
teaserFotkaMainXpath = "//*[@class='object-cover w-full h-full']"
destinationKostkyHPXpath = "//*[@class='c_tile-destination']"
itemsHPXpath ="//*[@class='items']"  ##destination items+3ikony nad patou
footerXpath = "//*[@class='footer-links']"

class Test_HP_D(unittest.TestCase):
    def setUp(self):
        setUp(self)
        self.test_passed = False

    def tearDown(self):
        if not self.test_passed:
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
        tearDown(self)
    def test_HP_D(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        wait = WebDriverWait(self.driver, 25)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(hlavickaMenuXpath)))
        assert (self.driver.find_element_by_xpath(hlavickaMenuXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(zlutakHPXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(teaserFotkaMainXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(itemsHPXpath)).is_displayed() == True
        assert (self.driver.find_element_by_xpath(footerXpath)).is_displayed() == True
        assert(1==2)
        self.test_passed = True