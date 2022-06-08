import time
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky, setUp, tearDown
import unittest

class TestPoznavacky_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_poznavacky_okruzni_D(self):
            self.driver.maximize_window()
            self.driver.get(URL_poznavacky)
            time.sleep(2)
            acceptConsent(self.driver)

            self.driver.execute_script("window.scrollTo(0, 1080);")

            time.sleep(6)
            self.driver.implicitly_wait(100)


            gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")

            y=0
            for _ in gridItems:

                gridItemDisplayed = gridItems[y].is_displayed()
                assert gridItemDisplayed == True
                y=y+1
                print("grid true")
            assert gridItems[0].is_displayed() == True


            gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
            a=0
            assert gridBig[0].is_displayed() == True
            for _ in gridBig:
                gridBigDisplayed = gridBig[a].is_displayed()
                assert gridBigDisplayed == True
                a=a+1
                print("big grid ture")

            self.test_passed = True

    def test_poznavacky_vikendy_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_vikendy)
        time.sleep(2)
        acceptConsent(self.driver)

        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(6)
        self.driver.implicitly_wait(100)

        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")

        y = 0
        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")
        assert gridItems[0].is_displayed() == True


        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")

        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True

        self.test_passed = True

    def test_poznavacky_rodiny_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_rodiny)
        time.sleep(2)
        acceptConsent(self.driver)
        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(8)


        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0

        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")
        assert gridItems[0].is_displayed() == True

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")

        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True
        self.test_passed = True

    def test_poznavacky_zazitky_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_zazitky)
        time.sleep(2)
        acceptConsent(self.driver)

        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(8)
        self.driver.implicitly_wait(100)


        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0

        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")

        assert gridItems[0].is_displayed() == True

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
        a = 0

        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

        assert gridBig[0].is_displayed() == True
        self.test_passed = True
