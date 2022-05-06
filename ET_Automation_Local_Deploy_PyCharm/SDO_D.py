from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,URL_SDO, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest
from ET_Automation_Local_Deploy_PyCharm.import_test_units_Xpaths import rowKarty_imgHoteluKarty_D

SDOsectionXpath = "//*[@class='sdo-section']"

def SDO_D(self, driver):
    generalDriverWaitImplicit(self.driver)
    rowKarty_imgHoteluKarty_D(self, self.driver)

    SDOsectionElement = self.driver.find_element_by_xpath(SDOsectionXpath)

    assert SDOsectionElement.is_displayed() == True
    print("sdo section visible true :  " + str(SDOsectionElement.is_displayed()))
class TestSDO_D(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SDO_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_SDO)

        time.sleep(0.3)
        acceptConsent(self.driver)
        SDO_D(self, self.driver)

        self.test_passed = True

