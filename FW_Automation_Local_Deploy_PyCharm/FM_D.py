from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_fmExotika, sendEmail, setUp, tearDown
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

#test
def LM_FM_vypis_rozbalit_zajezd_check(self, driver):
    wait = WebDriverWait(self.driver, 150000)
    driver.implicitly_wait(100)
    try:
        rozbal = self.driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
        wait.until(EC.visibility_of(rozbal))
        self.driver.execute_script("arguments[0].click();", rozbal)
        time.sleep(2)

    except NoSuchElementException:
        url = self.driver.current_url
        msg = " Nepodarilo se rozbalit FM zajezd " + url
        sendEmail(msg)

    try:
        rozbalenyZajezd = self.driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
        rozbalenyZajezdAll = self.driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
        wait.until(EC.visibility_of(rozbalenyZajezd))
        if rozbalenyZajezd.is_displayed():
            for WebElement in rozbalenyZajezdAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    pass

                else:
                    url = self.driver.current_url
                    msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
        sendEmail(msg)

    assert rozbalenyZajezd.is_displayed() == True



class TestFMexotika_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_exotika_D(self):
        self.driver.get(URL_fmExotika)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)
        try:
            zajezdyFMsingle = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            zajezdyFMall = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(zajezdyFMsingle))
            if zajezdyFMsingle.is_displayed():
                for WebElement in zajezdyFMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem s FM - zajezdy se neukazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s FM - zajezdy se neukazuji " + url
            sendEmail(msg)

        assert zajezdyFMsingle.is_displayed() == True
        self.test_passed = True
