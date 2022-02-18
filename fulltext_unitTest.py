from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, URL
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, wait
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
query = "Zanzibar"
URL_FT_results = URL+"/hledani-vysledky?q="
queryList = ["Zanzibar", "Mirage bay"]
class TestFulltext(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}


    def teardown_method(self, method):
        self.driver.quit()

    def test_fulltext_naseptavac(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        acceptConsent(self.driver)

        FTlupa = self.driver.find_element_by_xpath("//*[@class='f_anchor f_icon f_icon--magnifier']")
        FTlupa.click()

        inputBox = self.driver.find_element_by_xpath("//*[@class='f_input-item j_input']")
        inputBox.send_keys(query)
        time.sleep(2)
        # inputBox.send_keys(Keys.ENTER)

        prvniItem = self.driver.find_elements_by_xpath("//*[@class='f_item']")
        prvniItem[0].click()

        currentUrl = self.driver.current_url
        assert currentUrl != URL


    def test_fulltext_results_status_check(self):
        a=0
        for _ in queryList:
            driver = self.driver
            driver.get(URL_FT_results+queryList[a])
            if a==0:
                acceptConsent(driver)
            else:
                pass
            linksToCheckList = []
            vysledkyDlazdiceHotelu = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']/a")
            x = 0
            for _ in vysledkyDlazdiceHotelu:
                linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                x = x + 1

            vysledkyTextItems = driver.find_elements_by_xpath("//*[@class='f_fulltextResults-item']/a")
            z = 0
            for _ in vysledkyTextItems:
                linksToCheckList.append(vysledkyTextItems[0].text)
                z = z + 1

            print(linksToCheckList)
            a=a+1
            print(len(linksToCheckList))
            assert len(linksToCheckList) > 0
            y = 0
            for _ in linksToCheckList:
                response = requests.get(linksToCheckList[y])
                print(response.status_code)
                print(response.status_code == 200)
                assert response.status_code == 200
                y = y + 1