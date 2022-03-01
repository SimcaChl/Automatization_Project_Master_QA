from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, URL, setUp, tearDown
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, wait
import unittest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
query = "Mirage bay"
URL_FT_results = URL+"/hledani-vysledky?q="

querySDO = ["Zanzibar", "Řecko", "Turecko", "Egypt", "Kapverdy", "Oman" , "Maledivy", "Dubaj", "Mallorca", "Bulharsko", "Chorvatsko", "Kefalonia", "Attika" ]
queryCommon = ["pojištění",  "parkování", "covid", "Funtazie" ]
queryHotely = ["Mirage bay", "mitsis", "Prima life", "Prima life makadi", "Pegasos", "Pickalbatros", "Titanic", "mirage", "Domes Aulüs", "Bay & Mare",  "A for Art",
               "Porto Skala 7", "Costa Azzurra", "La Cite", "Naftilos", "Stefanos", "Magnolia",  "White Gold", "King Tut Resort", "Blue Waters",
               "Primasol", "Doubletree"]
queryList = querySDO+queryCommon+queryHotely
class TestFulltext(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_fulltext_naseptavac(self):
        wait = WebDriverWait(self.driver, 10)
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
            #inputBox.send_keys(queryList[poziceQueryItem])
            wait.until(EC.visibility_of(inputBox)).send_keys(queryList[poziceQueryItem])
            time.sleep(2)
            # inputBox.send_keys(Keys.ENTER)
            print(queryList[poziceQueryItem].upper())
            poziceQueryItem = poziceQueryItem+1


            #if self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']").isDisplayed()==True:
            #if hotelDlazdice != 0:
            try:
                    hotelDlazdice = self.driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
                    wait.until(EC.visibility_of(hotelDlazdice)).click()
                    #hotelDlazdice.click()
                    currentUrl = self.driver.current_url
                    assert currentUrl != URL
            except NoSuchElementException:
                prvniItem = self.driver.find_elements_by_xpath("//*[@class='f_item']")
                wait.until(EC.visibility_of(prvniItem[0])).click()
                #prvniItem[0].click()

                currentUrl = self.driver.current_url
                assert currentUrl != URL
            #else:





    def test_fulltext_results_status_check(self):
        wait = WebDriverWait(self.driver, 10)
        poziceQueryItem=0
        for _ in queryList:
            driver = self.driver
            driver.get(URL_FT_results+queryList[poziceQueryItem])
            if poziceQueryItem==0:
                acceptConsent(driver)
            else:
                pass
            print(queryList[poziceQueryItem].upper())
            linksToCheckList = []
            try:
                vysledkyDlazdiceHotelu = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']/a")
               # wait.until(EC.visibility_of(vysledkyDlazdiceHotelu[0]))
                x = 0
                for _ in vysledkyDlazdiceHotelu:
                    linksToCheckList.append(vysledkyDlazdiceHotelu[x].get_attribute("href"))
                    x = x + 1
            except NoSuchElementException:
                pass
            vysledkyTextItems = driver.find_elements_by_xpath("//*[@class='f_fulltextResults-item']/a")
            wait.until(EC.visibility_of(vysledkyTextItems[0]))
            z = 0
            for _ in vysledkyTextItems:
                    linksToCheckList.append(vysledkyTextItems[0].text)
                    z = z + 1

            #print(linksToCheckList)
            poziceQueryItem=poziceQueryItem+1
            #print(len(linksToCheckList))
            assert len(linksToCheckList) > 0        ## check if there are any result, length > 0
            y = 0
            #for _ in linksToCheckList:
            if len(linksToCheckList) > 5:
                for i in range(5):
                    response = requests.get(linksToCheckList[y])
                    #print(response.status_code)
                    #print(response.status_code == 200)
                    assert response.status_code == 200
                    y = y + 1
            else:
                for _ in linksToCheckList:
                    #print(response.status_code)
                    #print(response.status_code == 200)
                    assert response.status_code == 200
                    y = y + 1