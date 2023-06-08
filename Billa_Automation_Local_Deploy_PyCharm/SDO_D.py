from Billa_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,URL_SDO, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest


SDOsectionXpath = "//*[@class='sdo-section']"
zobrazitHotelyXpath = "//*[@class='c_title mb-0 center']"
SDOtlacitkoAndalusie = "//ul[@class='links']//a[normalize-space()='Andalusie']"

def SDO_oblast(self):
    self.driver.maximize_window()
    self.driver.get(URL_SDO)

    acceptConsent(self.driver)
    time.sleep(1)

    SDOtlacitkoElement = driver.find_element_by_xpath(SDOtlacitkoAndalusie).click()

    assert SDOtlacitkoElement.is_displayed() == True
    print("Andalusie se zobrazila")

def SDO_D(self, driver):
    generalDriverWaitImplicit(driver)
    SDOsectionElement = driver.find_element_by_xpath(SDOsectionXpath)

    assert SDOsectionElement.is_displayed() == True
    print("sdo section visible true :  " + str(SDOsectionElement.is_displayed()))
class TestSDO_D(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SDO_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_SDO)

        time.sleep(0.3)
        acceptConsent(self.driver)
        time.sleep(2)
        zobrazitHotelyElement = self.driver.find_element_by_xpath(zobrazitHotelyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", zobrazitHotelyElement)
        time.sleep(2.7)
        SDO_D(self, self.driver)

        self.test_passed = True



