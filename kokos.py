#obrazekZajimavaMistaXpath = "//*[@class='w-full relative pt-[60%]']"
#obrazekZajimavaMistaXpath = "//*[@class='absolute inset-0 object-cover w-full h-full']"
obrazekZajimavaMistaXpath ="//*[@class='shadow-lg transition-shadow rounded-md overflow-hidden flex flex-col justify-between no-underline text-inherit hover:shadow-[0_7px_20px_0px_rgba(0,0,0,0.16)]']"
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent


URL = "https://www.fischer.cz/arabske-emiraty/arabske-emiraty/dubaj/grand-hyatt-dubai#/zajimava-mista"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)

time.sleep(5)

acceptConsent(driver)
y=0
for _ in driver.find_elements_by_xpath(obrazekZajimavaMistaXpath):
    print(driver.find_elements_by_xpath(obrazekZajimavaMistaXpath)[y].is_displayed())
    y=y+1

time.sleep(20)