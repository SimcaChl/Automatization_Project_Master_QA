from selenium.webdriver.support.wait import WebDriverWait
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, setUp, tearDown, URL
from selenium.webdriver.support import expected_conditions as EC
import unittest

hlavickaMenuXpath = "//*[@class='inner']"
zlutakHPXpath = "//*[@class='f_filterMainSearch']"
teaserFotkaMainXpath = "//*[@class='object-cover w-full h-full']"
destinationKostkyHPXpath = "//*[@class='c_tile-destination']"
itemsHPXpath ="//*[@class='items']"  ##destination items+3ikony nad patou
footerXpath = "//*[@class='footer-links']"

class Test_HP_D(unittest.TestCase):
    def setUp(self):
        setUp(self)
        self.test_passed = False

    def tearDown(self):
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
        #assert(1==2)
        self.test_passed = True