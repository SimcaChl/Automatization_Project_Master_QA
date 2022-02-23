from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_kluby, sendEmail
from selenium import webdriver
import unittest
import pyautogui as p
p.FAILSAFE = False



class TestDetskeKluby_D(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()


    def test_kluby_D(self):
        self.driver.get(URL_kluby)
        acceptConsent(self.driver)
        self.driver.maximize_window()
        benefitItem = self.driver.find_elements_by_xpath("//*[@class='f_benefit-item splide__slide']")
        a=0
        for _ in benefitItem:
            benefitItemDisplay = benefitItem[a].is_displayed()
            a=a+1
            assert benefitItemDisplay == True
            print("benefit item")
        p.press("pagedown", presses=3)
        gridContainer = self.driver.find_elements_by_xpath("//*[@class='grd-container']")
        b=0
        for _ in gridContainer:
            gridContainerDisplay = gridContainer[b].is_displayed()
            assert  gridContainerDisplay == True
            b=b+1
            print ("grind container")
        p.press("pagedown", presses=2)
        tileImg = self.driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        c=0
        for _ in tileImg:
            tileImgDisplay = tileImg[c].is_displayed()
            assert tileImgDisplay == True
            c=c+1
            print("tile img")