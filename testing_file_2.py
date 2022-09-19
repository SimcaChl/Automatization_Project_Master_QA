import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent


driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://www.eximtours.cz/poznavaci-zajezdy"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)
gridItemXpath = "//*[@class='f_tileGrid-item']/a"
gridItemElements = driver.find_elements_by_xpath(gridItemXpath)
#print(URL_poznavaciho_hotelu)
linksToCheck_List = []
pozice=0
for _ in gridItemElements:
    odkazLink = gridItemElements[pozice].get_attribute("href")

    print(odkazLink)
    pozice = pozice+1
def generalized_list_of_url_checker(inputListOfURLStoCheck):
