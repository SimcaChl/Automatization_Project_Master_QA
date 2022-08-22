from selenium.webdriver.support.wait import WebDriverWait
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from EW_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from EW_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check

URL_deploying_web = URL
URL_prod_public = "https://www.eximtours.cz/"
banneryXpath_EW = "//*[@class='f_teaser-item js-priceUpdated']/a"

HPvyhledatZajezdyButtonXpath = "//*[contains(text(), 'Vyhledat zájezdy')]"
HPkamPojedeteButtonXpath = "//*[contains(text(), 'Kam se chystáte?')]"
HPzlutakReckoDestinaceXpath = "//*[@class='f_input-content'] //*[contains(text(), 'Řecko')]"
HPzlutakPokracovatButtonXpath = "//*[contains(text(), 'Pokračovat')]"
HPzlutakPokracovatButtonXpathStep2 = "//*[@class='f_filterHolder f_set--active'] //*[@class=('f_button-text f_icon f_icon--chevronRight f_icon_set--right')]"
HPzlutakLetniPrazdninyXpath = "//*[contains(text(), 'Podzimní prázdniny')]"
HPzlutakPridatPokojXpath = "//*[contains(text(), 'přidat pokoj')]"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
#HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']"
HPtopNabidkaXpath = "//*[@class='js-ajaxPlaceholder--widgetContent']/a"


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
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(2)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath))).click()
        time.sleep(1.3)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakReckoDestinaceXpath))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath))).click()
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakLetniPrazdninyXpath))).click()
        time.sleep(1.5)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2))).click()
        time.sleep(1.4)

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath))).click()

        time.sleep(1)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath))).click()
        time.sleep(2.789)
        SRL_D(self, self.driver)

        self.test_passed = True

    def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
           2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement = 0
        nejlepsiNabidkyTextList = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
            nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
            # print (nejlepsiNabidkyTextList)
            positionOfCurrentElement = positionOfCurrentElement + 1

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)))
        HPnejlepsiZajezdySwitchButtonElement = self.driver.find_element_by_xpath(HPnejlepsiZajezdySwitchButtonXpath)
        self.driver.execute_script("arguments[0].click();", HPnejlepsiZajezdySwitchButtonElement)
        time.sleep(6)
        time.sleep(6)
        self.driver.implicitly_wait(10)
        nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
        positionOfCurrentElement2 = 0
        nejlepsiNabidkyTextList2 = []
        for _ in nejlepsiNabidkyElement:
            nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement2].text
            nejlepsiNabidkyTextList2.append(nejlepsiNabidkyTextDefault)
            # print(nejlepsiNabidkyTextList)
            positionOfCurrentElement2 = positionOfCurrentElement2 + 1

        print(nejlepsiNabidkyTextList)
        print(nejlepsiNabidkyTextList2)
        assert nejlepsiNabidkyTextList != nejlepsiNabidkyTextList2

        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 25)
        self.driver.maximize_window()
        time.sleep(
            2.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        # wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnextArrowXpath))).click()
        # time.sleep(10)
        self.driver.implicitly_wait(100)
        topNabidkaBigHotelCardXpath  = "//*[@class='page-widget js-ajaxPlaceholder--widget fshr-widget f_tileGrid-item f_tileGrid-item--double']"
        topNabidkaBigHotelCardElement = self.driver.find_element_by_xpath(topNabidkaBigHotelCardXpath)

        self.driver.execute_script("arguments[0].scrollIntoView();", topNabidkaBigHotelCardElement )
        # self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        # action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(6)
        topNabidkaBigHotelCardElement.click()
        time.sleep(2)
        curURL = self.driver.current_url

        assert curURL != URL

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EW)

        self.test_passed = True



    def test_HP_top_nabidka_status(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        time.sleep(
            2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(10)
        generalized_EW_like_top_nabidka_URL_status_check(self.driver, HPtopNabidkaXpath)
