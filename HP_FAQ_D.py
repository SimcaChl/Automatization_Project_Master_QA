from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_covidInfo, sendEmail, URL, URL_faq, setUp, tearDown
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestHP_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)



    def test_homePage_isDisplayed(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        try:
            bannerSingle = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            bannerAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s bannery " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s bannery " + url
            sendEmail(msg)

        time.sleep(1.5)

        try:
            nejnabidkyLMsingle = self.driver.find_element_by_xpath("//*[@class='fshr-lm-table-item-content']")
            nejnabidkyLMall = self.driver.find_elements_by_xpath("//*[@class='fshr-lm-table-item-content']")
            wait.until(EC.visibility_of(nejnabidkyLMsingle))
            if nejnabidkyLMsingle.is_displayed():
                for WebElement in nejnabidkyLMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s nej. nabidky LM " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s nej. nabidky LM " + url
            sendEmail(msg)

        self.driver.get(URL_faq)

        try:
            faqSingle = self.driver.find_element_by_xpath("//*[@class='f_faq-item']")
            faqAll = self.driver.find_elements_by_xpath("//*[@class='f_faq-item']")
            if faqSingle.is_displayed():
                for WebElement in faqAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet==True
                    if jdouvidet == True:
                        pass
            else:
                url = self.driver.current_url
                msg = "Problem FAQ " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem FAQ " + url
            sendEmail(msg)