from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from to_import import acceptConsent, URL_groupsearch, setUp, tearDown,generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC


def groupSearch_D(self, driver):
    wait = WebDriverWait(self.driver, 150000)
    #driver.implicitly_wait(100)
    generalDriverWaitImplicit(driver)
    wait.until(EC.visibility_of(driver.find_element_by_xpath("//*[@class='f_teaser-item']")))

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

    assert teaserItems[0].is_displayed() == True

    driver.implicitly_wait(100)
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
    assert srlItems[0].is_displayed() == True


class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.get(URL_groupsearch)
        acceptConsent(self.driver)
        # teaserItems = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")



        groupSearch_D(self, driver)