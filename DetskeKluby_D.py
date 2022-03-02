from to_import import acceptConsent, URL_kluby, setUp, tearDown
import unittest
import pyautogui as p
p.FAILSAFE = False



class TestDetskeKluby_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_kluby_D(self):
        self.driver.get(URL_kluby)
        acceptConsent(self.driver)
        self.driver.maximize_window()
        benefitItem = self.driver.find_elements_by_xpath("//*[@class='f_benefit-item splide__slide']")
        assert benefitItem[0].is_displayed() == True
        a=0
        for _ in benefitItem:
            benefitItemDisplay = benefitItem[a].is_displayed()
            a=a+1
            assert benefitItemDisplay == True
            print("benefit item")
        p.press("pagedown", presses=3)
        gridContainer = self.driver.find_elements_by_xpath("//*[@class='grd-container']")
        b=0
        assert gridContainer[0].is_displayed() == True
        for _ in gridContainer:
            gridContainerDisplay = gridContainer[b].is_displayed()
            assert  gridContainerDisplay == True
            b=b+1
            print ("grind container")
        p.press("pagedown", presses=2)
        tileImg = self.driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        c=0
        assert tileImg[0].is_displayed() == True
        for _ in tileImg:
            tileImgDisplay = tileImg[c].is_displayed()
            assert tileImgDisplay == True
            c=c+1
            print("tile img")