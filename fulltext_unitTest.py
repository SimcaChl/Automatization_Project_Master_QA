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
query = "Mirage bay"
URL_FT_results = URL+"/hledani-vysledky?q="

queryStat = ["Zanzibar", "Řecko"]
queryHotely = ["Mirage bay"]
queryList = queryStat+queryHotely
class TestFulltext(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}


    def teardown_method(self, method):
        self.driver.quit()

    def test_fulltext_naseptavac(self):
        poziceQueryItem = 0
        for _ in queryList:
            self.driver.get(URL)
            self.driver.maximize_window()
            if poziceQueryItem==0:
                acceptConsent(self.driver)
            else:
                pass



            FTlupa = self.driver.find_element_by_xpath("//*[@class='f_anchor f_icon f_icon--magnifier']")
            FTlupa.click()

            inputBox = self.driver.find_element_by_xpath("//*[@class='f_input-item j_input']")
            inputBox.send_keys(queryList[poziceQueryItem])
            time.sleep(2)
            # inputBox.send_keys(Keys.ENTER)
            poziceQueryItem = poziceQueryItem+1

            prvniItem = self.driver.find_elements_by_xpath("//*[@class='f_item']")
            prvniItem[0].click()

            currentUrl = self.driver.current_url
            assert currentUrl != URL


    def test_fulltext_results_status_check(self):
        poziceQueryItem=0
        for _ in queryList:
            driver = self.driver
            driver.get(URL_FT_results+queryList[poziceQueryItem])
            if poziceQueryItem==0:
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
            poziceQueryItem=poziceQueryItem+1
            print(len(linksToCheckList))
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            for _ in linksToCheckList:
                response = requests.get(linksToCheckList[y])
                print(response.status_code)
                print(response.status_code == 200)
                assert response.status_code == 200
                y = y + 1