from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_pobocky, setUp, tearDown, generalDriverWaitImplicit
import time
import unittest

class TestPobocky_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_pobocky_D(self):

        self.driver.get(URL_pobocky)
        acceptConsent(self.driver)
        self.driver.maximize_window()
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        mapa = self.driver.find_element_by_xpath("//*[@class='leaflet-pane leaflet-tile-pane']")    ## jen jeden element, no need to call find_elementS

        mapaDisplayed = mapa.is_displayed()
        assert mapaDisplayed == True


        mapaKolecka = self.driver.find_elements_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
        y=0
        for _ in mapaKolecka:
            mapaKoleckaDisplayed = mapaKolecka[y].is_displayed()

            y=y+1
            print("mapa kolecka")
            assert mapaKoleckaDisplayed == True


        basicInfo = self.driver.find_elements_by_xpath("//*[@class='f_branch-basicInfo']")
        a=0
        assert basicInfo[0].is_displayed() == True
        for _ in basicInfo:
            basicInfoDisplay = basicInfo[a].is_displayed()

            print("basic info ")
            assert basicInfoDisplay == True
            a=a+1
        generalDriverWaitImplicit(self.driver)
        pobockaBoxiky = self.driver.find_elements_by_xpath("//*[@class='f_branch-header f_anchor']")
        x = 0
        for _ in pobockaBoxiky:
            pobockaBoxikyDisplay = pobockaBoxiky[x].is_displayed()

            print("boxiky")
            assert pobockaBoxikyDisplay == True
            x = x + 1

        assert pobockaBoxiky[0].is_displayed() == True
