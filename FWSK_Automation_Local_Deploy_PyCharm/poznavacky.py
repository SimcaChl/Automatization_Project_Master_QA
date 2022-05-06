import time
from FWSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky, setUp, tearDown, generalDriverWaitImplicit
import unittest

imgsXpath = "//*[@class='f_tile-image-content']"
gridItemsXpath = "//*[@class='f_tileGrid-item']"
gridBigXpath = "//*[@class='f_tileGrid']"


def poznavacky_check_D(self, driver):
    self.driver.maximize_window()
    generalDriverWaitImplicit(self.driver)
    generalDriverWaitImplicit(self.driver)
    time.sleep(7)
    imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
    #self.driver.execute_script("arguments[0].scrollIntoView();", kartyHoteluBottom)
    print(imgs)
    x = 0
    assert imgs[0].is_displayed() == True
    for _ in imgs:
        imgsDisplayed = imgs[x].is_displayed()
        x = x + 1

        assert imgsDisplayed == True
        print("true imgdisplay")

    gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
    self.driver.execute_script("arguments[0].scrollIntoView();", gridItems[0])
    assert gridItems[0].is_displayed() == True
    y = 0
    for _ in gridItems:
        gridItemDisplayed = gridItems[y].is_displayed()
        assert gridItemDisplayed == True
        y = y + 1
        print("grid true")

    gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
    a = 0
    assert gridBig[0].is_displayed() == True
    for _ in gridBig:
        gridBigDisplayed = gridBig[a].is_displayed()
        assert gridBigDisplayed == True
        a = a + 1
        print("big grid ture")

class TestPoznavacky_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_poznavacky_okruzni_D(self):
            self.driver.get(URL_poznavacky)

            acceptConsent(self.driver)
            poznavacky_check_D(self, self.driver)
            self.test_passed = True

    def test_poznavacky_zazitky_D(self):
        self.driver.get(URL_poznavacky_zazitky)

        acceptConsent(self.driver)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True
    def test_poznavacky_vikendy_D(self):
        self.driver.get(URL_poznavacky_vikendy)
        acceptConsent(self.driver)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True

    def test_poznavacky_rodiny_D(self):
        self.driver.get(URL_poznavacky_rodiny)
        acceptConsent(self.driver)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True
