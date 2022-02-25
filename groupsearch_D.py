from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_covidInfo, sendEmail, URL, URL_faq, URL_lm, URL_stat, URL_groupsearch, setUp, tearDown
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest



class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 150000)
        self.driver.get(URL_groupsearch)
        acceptConsent(self.driver)
        teaserItems = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")

        try:
            for WebElement in teaserItems:
                ##print(len(teaserItems))
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    ##print(jdouvidet)
                    ##print(WebElement)
                    pass

                else:
                    pass
                    ##print("Else")
                    ##emailfunciton

        except NoSuchElementException:
            pass
            ##print("no such")
            ##email fnction

        srlItems = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]")
        try:
            for WebElement in srlItems:
                ##print(len(srlItems))
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    ##print(jdouvidet)
                    ##print(WebElement)
                    pass

                else:
                    pass
                    print("Else")



        except NoSuchElementException:
            pass
            print("no such")
