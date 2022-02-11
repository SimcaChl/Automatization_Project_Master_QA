import pytest
import time
import json
from selenium import webdriver

from to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky
from threading import Thread
from to_import_secret import comandExecutor
desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"browserstack.local" : "false",
"browserstack.selenium_version" : "3.5.2"
}


class TestPoznavacky_D():

    def setup_method(self, method):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Remote(
        command_executor=comandExecutor,desired_capabilities=desired_cap )
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_poznavacky_okruzni_D(self):
            self.driver.get(URL_poznavacky)

            acceptConsent(self.driver)
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(0, 1080);")

            time.sleep(6)
            imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
            print(imgs)
            x=0
            for _ in imgs:
                imgsDisplayed = imgs[x].is_displayed()
                x=x+1

                assert imgsDisplayed == True
                print("true imgdisplay")

            gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
            y=0
            for _ in gridItems:

                gridItemDisplayed = gridItems[y].is_displayed()
                assert gridItemDisplayed == True
                y=y+1
                print("grid true")

            gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
            a=0
            for _ in gridBig:
                gridBigDisplayed = gridBig[a].is_displayed()
                assert gridBigDisplayed == True
                a=a+1
                print("big grid ture")

    def test_poznavacky_vikendy_D(self):
        self.driver.get(URL_poznavacky_vikendy)

        acceptConsent(self.driver)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(6)
        imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
        print(imgs)
        x = 0
        for _ in imgs:
            imgsDisplayed = imgs[x].is_displayed()
            x = x + 1

            assert imgsDisplayed == True
            print("true imgdisplay")

        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0
        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

    def test_poznavacky_rodiny_D(self):
        self.driver.get(URL_poznavacky_rodiny)

        acceptConsent(self.driver)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(6)
        imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
        print(imgs)
        x = 0
        for _ in imgs:
            imgsDisplayed = imgs[x].is_displayed()
            x = x + 1

            assert imgsDisplayed == True
            print("true imgdisplay")

        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0
        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

    def test_poznavacky_zazitky_D(self):
        self.driver.get(URL_poznavacky_zazitky)

        acceptConsent(self.driver)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 1080);")

        time.sleep(6)
        imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
        print(imgs)
        x = 0
        for _ in imgs:
            imgsDisplayed = imgs[x].is_displayed()
            x = x + 1

            assert imgsDisplayed == True
            print("true imgdisplay")

        gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
        y = 0
        for _ in gridItems:
            gridItemDisplayed = gridItems[y].is_displayed()
            assert gridItemDisplayed == True
            y = y + 1
            print("grid true")

        gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
        a = 0
        for _ in gridBig:
            gridBigDisplayed = gridBig[a].is_displayed()
            assert gridBigDisplayed == True
            a = a + 1
            print("big grid ture")

Thread(target=TestPoznavacky_D, args=(desired_cap,)).start()