from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from to_import import acceptConsent, URL, caps, closeExponeaBanner


URL = "https://v2.nev-dama.cz/zima/pokusna_zeme/pokusne-stredisko-zima/pokusna-rezidence/rezervaceNova?termin=2021-03-20&typologie=[9002]&delka=7"
URL2 = "https://v2.nev-dama.cz/zima/pokusna_zeme/pokusne-stredisko-zima/pokusna-rezidence/rezervaceNova?termin=2021-03-13&typologie=[9002]&delka=7"
URL3 = "https://v2.nev-dama.cz/zima/pokusna_zeme/pokusne-stredisko-zima/pokusny-hotel-l"
prijmeni = "Tester"
telefon = "735599725"
email = "ondrej.kadoun@fischer.cz"
ulice = "Chebska"
PSC = "12345"
mesto = "Praha"
rok = "2000"

def udelejKosik():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
    driver.get(URL3)
    wait = WebDriverWait(driver, 80)

    driver.maximize_window()
    ##driver.find_element_by_xpath("//body/a[1]/span[3]").click()
    ##driver.find_element_by_xpath("//*[@class='exponea-close-cross']").click()       ## double close
    ##driver.find_element_by_xpath("//*[@class='exponea-close-cross']").click()
    ##driver.find_element_by_xpath("//*[@id='allow-cookies-button']").click()
    time.sleep(1)
    acceptConsent(driver)
    time.sleep(1)
    closeExponeaBanner(driver)

    mamZajemBtn = driver.find_element_by_xpath("//*[@class='fshr-hotelLayout--right'] //*[@class='fshr-hotelReserve']")
    mamZajemBtn.click()
    ##driver.execute_script("arguments[0].click();", mamZajemBtn)


    form = driver.find_element_by_xpath("//div[@id='koupit-online']")  ##Koupit online
    form.find_element_by_id("surname003").send_keys(prijmeni)
    form.find_element_by_id("phone03").send_keys(telefon)
    form.find_element_by_id("email03").send_keys(email)
    driver.find_element_by_xpath("//button[contains(text(),'Pokračovat online')]").click()
    time.sleep(10)

    wait.until(EC.presence_of_element_located((By.ID, 'Ulice')))
    driver.find_element_by_id("Ulice").send_keys(ulice)
    driver.find_element_by_id("CisloPopisne").send_keys(PSC)  ##1
    driver.find_element_by_id("Psc").send_keys(PSC)
    driver.find_element_by_id("Mesto").send_keys(mesto)
    ##driver.find_element_by_id("DatumRok").send_keys(rok)
    ##driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()
    dalsiKrok = driver.find_element_by_xpath("//button[contains(text(),'Další krok')]")
    driver.execute_script("arguments[0].click();", dalsiKrok)

    wait.until(EC.presence_of_element_located((By.ID, "krok2_9002_0_0_1_Skipas")))
    driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()  ##2 predvyplnene udaje
    time.sleep(20)

    time.sleep(15)
    ##wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Další krok')]")))
    ##driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()                     ##3 jen click dal, no IDS
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='js-kosik-form form-krok3']//button[contains(text(),'Další krok')]")))
    driver.find_element_by_xpath("//*[@class='js-kosik-form form-krok3']//button[contains(text(),'Další krok')]").click()


    wait.until(EC.presence_of_element_located((By.ID, "krok4_6_sluzba")))
    checkboxPostylka = driver.find_element_by_xpath("//*[@type='checkbox' and @id='krok4_6_sluzba']")               ##4 sluzby
    driver.execute_script("arguments[0].click();", checkboxPostylka)
    checkboxSnowboard = driver.find_element_by_xpath("//*[@type='checkbox' and @id='krok4_238_sluzba']")
    time.sleep(3)
    driver.execute_script("arguments[0].click();", checkboxSnowboard)
    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()
    time.sleep(11)

    wait.until(EC.presence_of_element_located((By.ID, "krok4_Optimal P4_sluzba")))              ##5 pojisteni
    checkboxOptimalP2 = driver.find_element_by_id("krok4_Optimal P4_sluzba")
    driver.execute_script("arguments[0].click();", checkboxOptimalP2)
    driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()
    time.sleep(5)

    wait.until(EC.presence_of_element_located((By.NAME, "cislo_voucheru")))
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'Další krok')]").click()                             ##6 skip voucher

    wait.until(EC.presence_of_element_located((By.ID, "krok5_InformacniMemorandum")))
    memorandum = driver.find_element_by_id("krok5_InformacniMemorandum")
    osobniUdaje = driver.find_element_by_id("krok5_PredavaniOsobnichUdaju")
    podminky = driver.find_element_by_id("krok5_VseobecnePodminky")
    driver.execute_script("arguments[0].click();", memorandum)
    driver.execute_script("arguments[0].click();", osobniUdaje)
    driver.execute_script("arguments[0].click();", podminky)

    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(),'Dokončit objednávku')]").click()
    time.sleep(150)


udelejKosik()
