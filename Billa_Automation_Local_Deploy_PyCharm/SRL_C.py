from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from Billa_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_SRL, sendEmail, setUp, tearDown, returnLocatorForMealHotelKarty, generalDriverWaitImplicit, URL_SRL_all_inclusive
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pyautogui as p

p.FAILSAFE = False
totalPriceXpath = "//*[@class='price-amount']"
odNejdrazsihoSorterXpath = "//*[contains(text(), 'od nejdražšího')]"
zobrazitNaMapeXpath = "//*[@class='c_btn white']"
detailHoteluButtonXpath = "//*[@class='c_btn inline ellipsis green']"
detailHoteluCenaAllXpath = "//*[@class='text-h3 text-green font-bold']"
detailHoteluCross = "//*[@class='f_icon f_icon--cross']"
chatCrossXpath = "//*[@id='daktela-web-greeting-close']"
#SDO_Strava_row_karta_hotelu_Xpath = "//*[@class='c_row'][2]"
SDO_Strava_row_karta_hotelu_Xpath = "//*[@class='c_row']/span/i"

from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble

returnLocatorForMealHotelKarty(1)
class Test_SRL_C(unittest.TestCase):
    def setUp(self):
        setUp(self)
    def tearDown(self):
        tearDown(self)
    def test_SRL_sort_cheapest(self):
        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 150)
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(4)
        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
        poziceHotelu =0
        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            #cenaZajezduAllString = cenaZajezduAllString[:-3]
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort()  ##sorting second list low to high

        if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
            print("Razeni od nejlevnejsiho je OK")

        else:
            print("Razeni od nejlevnejsiho je spatne")

        print(cenaZajezduAllList)
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True

    def test_SRL_sort_expensive(self):
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(3)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(odNejdrazsihoSorterXpath))).click()
        time.sleep(4.5)   ##waits not working, for now just time sleep

        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(totalPriceXpath)))
        cenaZajezduAllList = []  ##one list that takes prices from the srl
        cenaZajezduAllListSorted = []
        cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)


        poziceHotelu = 0

        for WebElement in cenaZajezduAll:
            cenaZajezduAllString = cenaZajezduAll[poziceHotelu].text
            cenaZajezduAllString = ''.join(cenaZajezduAllString.split())  ##delete spaces
            cenaZajezduAllString = int(cenaZajezduAllString)  ##convert to int to do sort easily
            poziceHotelu = poziceHotelu + 1
            cenaZajezduAllList.append(cenaZajezduAllString)
            cenaZajezduAllListSorted.append(cenaZajezduAllString)

        cenaZajezduAllListSorted.sort(reverse=True)

        if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
            print("Razeni od nejdrazsiho je OK")

        else:
            print("Razeni od nejdrazsiho je spatne")

        print(cenaZajezduAllList)
        print(cenaZajezduAllListSorted)

        assert cenaZajezduAllListSorted == cenaZajezduAllList

        self.test_passed = True

    def test_SRL_map(self):
        driver = self.driver
        driver.get(URL_SRL)
        wait = WebDriverWait(driver, 12)
        time.sleep(5)
        self.driver.maximize_window()
        acceptConsent(driver)
        time.sleep(10)
        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(zobrazitNaMapeXpath))).click()
        generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath)
        time.sleep(3)

        generalized_map_test_click_on_pin_and_hotel_bubble(self.driver)


        #assert (self.driver.current_url) != URL_SRL
        self.driver.switch_to.window(self.driver.window_handles[1]) ##gotta switch to new window
        currentUrl = self.driver.current_url
        print(currentUrl)
        print(URL_SRL)
        assert currentUrl != URL_SRL

        self.test_passed = True

    def test_SRL_filtr_strava(self):
        driver = self.driver
        driver.get(URL_SRL_all_inclusive)
        #driver.get(URL_SRL)
        wait = WebDriverWait(driver, 12)
        time.sleep(5)
        self.driver.maximize_window()
        acceptConsent(driver)
        time.sleep(2)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(SDO_Strava_row_karta_hotelu_Xpath)))
        SDOstravaRowKartaElement = self.driver.find_elements_by_xpath(SDO_Strava_row_karta_hotelu_Xpath)
        x=1
        time.sleep(5)
        #for _ in SDOstravaRowKartaElement:
        #for _ in (self.driver.find_elements_by_xpath(detailHoteluCenaAllXpath)):
        for i in range(19):
            stravaHoteluXpathCreator = returnLocatorForMealHotelKarty(x)
            #print(stravaHoteluXpathCreator)
            stravaHoteluVkarte = self.driver.find_elements_by_xpath(stravaHoteluXpathCreator)

            stravaHoteluVkarteAssertValue = stravaHoteluVkarte[0].text.lower()
            #print(stravaHoteluVkarteAssertValue)
            #assert stravaHoteluVkarteAssertValue == "all inclusive"
            assert("all inclusive" in stravaHoteluVkarteAssertValue)
            #print(stravaHoteluVkarte[0])
            #print(SDOstravaRowKartaElement[x].text)
            x=x+1


        self.test_passed = True

    def test_srl_C(self):
        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        #wait = WebDriverWait(self.driver, 150000)
        wait = WebDriverWait(self.driver, 20)


        time.sleep(3)

        acceptConsent(self.driver)

        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(chatCrossXpath)).click())
        generalDriverWaitImplicit(self.driver)
        #self.driver.find_element_by_xpath(chatCrossXpath).click()
        #wait.until(EC.visibility_of(self.driver.find_element_by_xpath(chatCrossXpath))).click()
        time.sleep(6)
        try:
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[1]))
        except NoSuchElementException:
            url = self.driver.current_url
            msg = " Problem SRL hotelyAllKarty" + url
            sendEmail(msg)
        x = 0
        #for WebElement in self.driver.find_elements_by_xpath(totalPriceXpath):
        for i in range(3):
            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[0]))
            cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
            cenaZajezduAllString = cenaZajezduAll[x].text
            print(cenaZajezduAllString)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(detailHoteluButtonXpath)[x])).click()
            time.sleep(5)
            detailCenaAll = self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)))
            detailCenaAllString = detailCenaAll.text
            detailCenaAllString = detailCenaAllString[:-3]
            print(detailCenaAllString)
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")
            else:
                print("ceny all NESEDÍ srl vs detail")
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCross))).click()
            x = x + 1
            print(x)

        #p.press("pagedown")
        detailHoteluButtonElement = self.driver.find_elements_by_xpath(detailHoteluButtonXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", detailHoteluButtonElement[x])

        time.sleep(3.5)
        x=5
        for i in range(4):
            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[0]))
            cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
            cenaZajezduAllString = cenaZajezduAll[x].text
            print(cenaZajezduAllString)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(detailHoteluButtonXpath)[x])).click()
            time.sleep(5)
            detailCenaAll = self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)))
            detailCenaAllString = detailCenaAll.text
            detailCenaAllString = detailCenaAllString[:-3]
            print(detailCenaAllString)
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")
            else:
                print("ceny all NESEDÍ srl vs detail")
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCross))).click()
            x = x + 1
            print(x)



        time.sleep(1)
        x = 10
        for i in range(3):
            print("|||||HOTEL CISLO|||||||")
            print(x + 1)
            print(x + 1)
            print(x + 1)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[0]))
            cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
            cenaZajezduAllString = cenaZajezduAll[x].text
            print(cenaZajezduAllString)
            wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(detailHoteluButtonXpath)[x])).click()
            time.sleep(5)
            detailCenaAll = self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)))
            detailCenaAllString = detailCenaAll.text
            detailCenaAllString = detailCenaAllString[:-3]
            print(detailCenaAllString)
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")
            else:
                print("ceny all NESEDÍ srl vs detail")
            wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCross))).click()
            x = x + 1
            print(x)

        #p.press("pagedown")
        # detailHoteluButtonElement = self.driver.find_elements_by_xpath(detailHoteluButtonXpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", detailHoteluButtonElement[x])
        # time.sleep(1)
        # x = 15
        # for i in range(4):
        #     print("|||||HOTEL CISLO|||||||")
        #     print(x + 1)
        #     print(x + 1)
        #     print(x + 1)
        #     wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(totalPriceXpath)[0]))
        #     cenaZajezduAll = self.driver.find_elements_by_xpath(totalPriceXpath)
        #     cenaZajezduAllString = cenaZajezduAll[x].text
        #     print(cenaZajezduAllString)
        #     wait.until(EC.visibility_of(self.driver.find_elements_by_xpath(detailHoteluButtonXpath)[x])).click()
        #     time.sleep(5)
        #     detailCenaAll = self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)
        #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCenaAllXpath)))
        #     detailCenaAllString = detailCenaAll.text
        #     detailCenaAllString = detailCenaAllString[:-3]
        #     print(detailCenaAllString)
        #     assert detailCenaAllString == cenaZajezduAllString
        #     if detailCenaAllString == cenaZajezduAllString:
        #         print("ceny all sedi srl vs detail")
        #     else:
        #         print("ceny all NESEDÍ srl vs detail")
        #     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(detailHoteluCross))).click()
        #     x = x + 1
        #     print(x)

        self.test_passed = True
