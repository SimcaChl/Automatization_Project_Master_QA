from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest


#URL_detail = "https://www.fischer.cz/recko/lefkada/agios-nikitas/olive-tree-ct?DS=1&D=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=628177&MT=1&DI=49&RT=15&NN=7&RD=2022-08-18&DD=2022-08-11&DP=2682&TO=4312|4305|2682|4308&MNN=7|8|9|10|11|12|13&TT=1&PID=LFOLISO&DPR=Fischer&TTM=1&TOM=4312|4305|2682|4308&DF=2022-08-11|2022-09-11&ERM=0&NNM=7|8|9|10|11|12|13&ac1=3&kc1=0&ic1=0"
#URL_detail = "https://www.fischer.cz/recko/lefkada/agios-nikitas/olive-tree-ct?DS=1&D=826|1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=628177&MT=1&DI=49&RT=15&NN=7&RD=2022-08-18&DD=2022-08-11&DP=4305&TO=4305&MNN=7|8|9|10|11&TT=1&PID=LFOLISO&DPR=Fischer&TTM=1&DF=2022-08-11|2022-09-11&ERM=0&NNM=7|8|9|10|11&ac1=2&kc1=0&ic1=0#/terminy"
class TestDetail_C(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def omlouvamese_paragraph(self):
        time.sleep(1)
        try:
            omlouvameParagraph = self.driver.find_element_by_xpath(
                "//*[@class='fshr-paragraph fshr-paragraph--centered']")
            if omlouvameParagraph.is_displayed():
                return

        except NoSuchElementException:
            pass

    def test_detail_fotka(self):

        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(1)
        closeExponeaBanner(self.driver)

        imageDetail = self.driver.find_element_by_xpath("//*[@id='gallery01Trigger']//img")
        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            image = self.driver.find_element_by_xpath("/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                print("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

    def test_detail_terminy_filtr_meal(self):

        def omlouvamese_paragraph(self):
            time.sleep(1)
            try:
                omlouvameParagraph = self.driver.find_element_by_xpath(
                    "//*[@class='fshr-paragraph fshr-paragraph--centered']")
                if omlouvameParagraph.is_displayed():
                    return

            except NoSuchElementException:
                pass

        self.driver.get(URL_detail)
        wait = WebDriverWait(self.driver, 150000)
        acceptConsent(self.driver)

        time.sleep(1)
        closeExponeaBanner(self.driver)

        try:
            terminyCeny = self.driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            ##terminyCeny.click()
            self.driver.execute_script("arguments[0].click();", terminyCeny)
            try:
                potvrdit = self.driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")

                self.driver.execute_script("arguments[0].click();", potvrdit)

            except NoSuchElementException:
                url = self.driver.current_url
                msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
                sendEmail(msg)


        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
            sendEmail(msg)

        try:
            stravovaniBox = self.driver.find_element_by_xpath(
                "//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']")
            wait.until(EC.visibility_of(stravovaniBox))
            self.driver.execute_script("arguments[0].click();", stravovaniBox)
            try:
                # allInclusiveBox =
                # driver.find_element_by_xpath("//*[contains(text(), 'All
                # inclusive')]")
                # wait.until(EC.visibility_of(allInclusiveBox))
                ##allInclusiveBox.click()
                stravyBox = self.driver.find_elements_by_xpath("//*[@name='detailFilterCatering']")

                self.driver.execute_script("arguments[0].click();", stravyBox[1])

                try:
                    ##potvrditButtonBox =
                    ##driver.find_element_by_xpath("//*[@class='fshr-filter-footer']
                    ##//*[contains(text(), 'Potvrdit')]")

                    # potvrditButtonBox.click()
                    self.driver.execute_script("arguments[0].click();",
                                               stravovaniBox)  ##workaround, klikni na box to confirm the choice

                except NoSuchElementException:
                    url = self.driver.current_url
                    msg = "stravaBox, potvrzeni stravy na detailu hotelu problém, NoSuchElementException " + url
                    sendEmail(msg)

            except NoSuchElementException:
                url = self.driver.current_url
                msg = "allInclusiveBox, zvolení stravy na detailu hotelu problém, NoSuchElementException " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "stravovaniBox, otevření filtru stravování detail hotelu, NoSuchElementException " + url
            sendEmail(msg)

        #omlouvamese_paragraph(self)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath("//*[@class='js-subvalue f_text--highlighted']")
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text

        print(zvolenaStravaVboxuString)

        stravaVterminech = self.driver.find_elements_by_xpath(
            "//*[@class='fshr-termin-catering js-tooltip js-tooltip--onlyDesktop']")
        stravaVterminechString = []

        ##ty for loopy se nezapnou pokud pocet vysledku bude 0
        ##takze treba exim a dx bude casto takto jelikoz se tam nabizi vsechny
        ##stravy, ne jen ty available
        x = 0
        for _ in stravaVterminech:
            stringos = stravaVterminech[x].text
            stravaVterminechString.append(stringos)
            x = x + 1

        time.sleep(1)  ###eroror element is not attached ?  tak chvilku cekacka mozna to solvne

        print(stravaVterminechString)
        y = 0
        for _ in stravaVterminechString:
            assert stravaVterminechString[y] == zvolenaStravaVboxuString
            if stravaVterminechString[y] == zvolenaStravaVboxuString:
                print("ok")
                ##print(y)
                y = y + 1
            else:
                url = self.driver.current_url
                msg = "na detailu jsem vyfiltroval stravu " + zvolenaStravaVboxuString + "ale pry to nesedi říká python" + url
                sendEmail(msg)
                y = y + 1
        time.sleep(1)
        ##print(stravaVterminech)
        ##print(stravaVterminechString)

    def test_detail_terminy_filtr_airport(self):

        def omlouvamese_paragraph(self, driver):
            time.sleep(1)
            try:
                omlouvameParagraph = self.driver.find_element_by_xpath(
                    "//*[@class='fshr-paragraph fshr-paragraph--centered']")
                if omlouvameParagraph.is_displayed():
                    return

            except NoSuchElementException:
                pass


        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(1)
        closeExponeaBanner(self.driver)
        wait = WebDriverWait(self.driver, 150000)

        try:
            terminyCeny = self.driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            ##terminyCeny.click()
            self.driver.execute_script("arguments[0].click();", terminyCeny)
            time.sleep(0.5)
            try:
                potvrdit = self.driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
                ##wait.until(EC.visibility_of(potvrdit))
                self.driver.execute_script("arguments[0].click();", potvrdit)

            except NoSuchElementException:
                url = self.driver.current_url
                msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
            sendEmail(msg)

        try:
            dopravaBox = self.driver.find_element_by_xpath(
                "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']")
            wait.until(EC.visibility_of(dopravaBox))
            self.driver.execute_script("arguments[0].click();", dopravaBox)
            try:
                dopravaBrno = self.driver.find_element_by_xpath(
                    "//*[@data-value='4305']")  ##natvrdo brno, no list shenanigans
                self.driver.execute_script("arguments[0].click();", dopravaBrno)

                time.sleep(0.5)
                try:
                    ##potvrditButtonBox =
                    ##driver.find_element_by_xpath("//*[@class='fshr-filter-footer']
                    ##//*[contains(text(), 'Potvrdit')]")
                    ##potvrditButtonBox =
                    ##driver.find_element_by_xpath("//*[@class='fshr-button
                    ##fshr-button--commonImportance fshr-button--big
                    ##js-filterClose']")
                    ##potvrditButtonBox =
                    ##driver.find_element_by_xpath("//*[@class='js-filter
                    ##js-filter--detail fshr-filter fshr-filter--travel
                    ##js-change-detection
                    ##fshr-filter--active']//*[@class='fshr-filter-wrapper
                    ##js-filter-window']//*[@class='fshr-filter-footer']//*[@class='fshr-button
                    ##fshr-button--commonImportance fshr-button--big
                    ##js-filterClose']")
                    ##wait.until(EC.visibility_of(potvrditButtonBox))
                    # potvrditButtonBox.click()
                    self.driver.execute_script("arguments[0].click();",
                                               dopravaBox)  ##workaround, proste klikne znova na doprava box aby se to propsalo, potvrdit
                    ##button mi nejak blbnul
                    ##driver.execute_script("arguments[0].click();",
                    ##potvrditButtonBox)

                except NoSuchElementException:
                    url = self.driver.current_url
                    msg = "potvrditButtonBox, potvrzeni dopravy na detailu hotelu problém, NoSuchElementException " + url
                    sendEmail(msg)

            except NoSuchElementException:
                url = self.driver.current_url
                msg = "dopravaBrno, zvolení dopravy na detailu hotelu problém, NoSuchElementException " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "dopravaBox, zvolení dopravy na detailu hotelu problém, NoSuchElementException " + url
            sendEmail(msg)

        time.sleep(1)  ##cekacka na terminy load
        omlouvamese_paragraph(self, self.driver)

        try:
            pocetZobrazenychTerminu = self.driver.find_elements_by_xpath(
                "//*[@class='fshr-termins-table-item-header js-toggleSlide']")  ##locator jen na pocet odletu alokuje vic veci nez je actual terminu tak
            ##pro
            ##for
            ##loop
            ##pouziju
            ##tohle
            ##=
            ##20
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "pocetZobrazenychTerminu, filtrovani dle letu detail hotelu, mozna jen nema odlety na X, NoSuchElementException " + url
            sendEmail(msg)

        try:
            odletyTerminy = self.driver.find_elements_by_xpath(
                "//*[@class='fshr-termin-departure-from']")  ##prvni locator je "odlet" takze zacnu na pozici jedna, vyloopuje se to podle
            ##poctu terminu, should be ok
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "odletyTerminy, nejsou odlety na brno, most likely not a bad thing, NoSuchElementException " + url
            sendEmail(msg)
        y = 1
        for _ in pocetZobrazenychTerminu:
            assert odletyTerminy[y].text == "Brno"
            if odletyTerminy[y].text == "Brno":  ##tady je nutny pricitat +2 protoze je tam 41 results (s tim ze jeden
                ##je "odlet"), kazdy sudy cislo je mezera/blank space for some reason
                ##print(odletyTerminy[y].text)
                y = y + 2
            else:
                url = self.driver.current_url
                ##print(odletyTerminy[y].text)
                msg = "na detailu jsem vyfiltroval odlet na brno ale pry to nesedi říká python " + url
                sendEmail(msg)
                y = y + 2

