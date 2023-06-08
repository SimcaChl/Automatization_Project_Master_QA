from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from Billa_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from Billa_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from Billa_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from Billa_Automation_Local_Deploy_PyCharm.SDO_D import SDO_D

HPvyhledatZajezdyButtonXpath = "//*[@class='f_filterMainSearch'] //*[contains(text(), 'Vyhledat dovolenou')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam se chystáte?')]"
HPzlutakEgyptDestinaceXpath = "//*[@class='f_filterMainSearch']//*[@class='flex flex-row overflow-hidden']//*[@class='flex flex-col pb-2']//*[contains(text(), 'Egypt')]"
HPzlutakPokracovatButtonXpath = "//div[@class='f_filterHolder js_filterHolder f_set--active'] //div//a[@class='c_btn primary'][contains(text(),'Pokračovat')]"
HPzlutakTypDopravyPokracovat = "//div[@class='f_filterHolder js_filterHolder f_set--active'] //div//a[@class='c_btn primary'][contains(text(),'Pokračovat')]"
HPzlutakKdyPojedetePokracovat = "//div[@class='f_filterHolder js_filterHolder f_set--active'] //div//a[@class='c_btn primary'][contains(text(),'Pokračovat')]"
HPzlutakObsazenost2plus2Xpath = "//*[contains(text(), 'Rodina')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_filterHolder js_filterHolder f_set--active']//*[contains(text(), 'Potvrdit a vyhledat')]"
HPstatyKartyXpath = "//*[@class='content']"
HPdlazdiceRecko = "//h2[contains(text(),'Řecko')]"
HPdlazdiceChorvatsko = "//h2[contains(text(),'Chorvatsko')]"
HPdlazdiceItalie = "//h2[normalize-space()='Romantická Itálie']"

class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HP_zlutak_to_groupsearch(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)     ##time sleep not the best not pog but it works =)
        groupSearch_D(self, self.driver)
        self.test_passed = True


    def test_HP_zlutak_to_SRL(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click() #kam pojedete
        time.sleep(0.3)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakEgyptDestinaceXpath))).click() #kliknu na Egypt
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click() #dam pokracovat
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakTypDopravyPokracovat))).click() #jak cestujete, kliknu na pokracovat

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakKdyPojedetePokracovat))).click() #kdy pojedete, kliknu na pokracovat
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus2Xpath))).click() #kolik vas bude, kliknu na Rodina

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click() #kliknu na potvrdit a vyhledat
        SRL_D(self, self.driver)

        self.test_passed = True


    def test_HP_banner_destination_to_SDO(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        acceptConsent(self.driver)
        time.sleep(1)
        HPstatyKartyElement=self.driver.find_element_by_xpath(HPstatyKartyXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPstatyKartyElement)

        time.sleep(0.666)
        HPstatyKartyElement.click()
        time.sleep(6.666)
        SDO_D(self, self.driver)

        self.test_passed = True

    def test_dlazdice_Recko(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        acceptConsent(self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath(HPdlazdiceRecko).click()
        time.sleep(5)
        EC.title_contains("Výsledky hledání zájezdů")

        expected_title = "Výsledky hledání zájezdů"
        actual_title = self.driver.title

        if expected_title in actual_title:
            print("Jsem na stránce se zájezdy")
        else:
            print("Zájezdy se nezobrazily")
    def test_dlazdice_Chorvatsko(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        acceptConsent(self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath(HPdlazdiceChorvatsko).click()
        time.sleep(5)
        EC.title_contains("Výsledky hledání zájezdů")

        expected_title = "Výsledky hledání zájezdů"
        actual_title = self.driver.title

        if expected_title in actual_title:
            print("Jsem na stránce se zájezdy")
        else:
            print("Zájezdy se nezobrazily")

    def test_dlazdice_Italie(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        acceptConsent(self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath(HPdlazdiceItalie).click()
        time.sleep(5)
        EC.title_contains("Výsledky hledání zájezdů")

        expected_title = "Výsledky hledání zájezdů"
        actual_title = self.driver.title

        if expected_title in actual_title:
            print("Jsem na stránce se zájezdy")
        else:
            print("Zájezdy se nezobrazily")
