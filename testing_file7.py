import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())
URL_detail = "https://www.fischer.cz/spanelsko/mallorca/alcudia/mariant?DS=256&GIATA=21437&D=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&HID=21&MT=5&NN=7&DF=2023-10-01|2023-10-31&RD=2023-10-14&DD=2023-10-07&ERM=0&AC1=2&KC1=1&KA1=10&IC1=1&AC2=2&KC2=2&KA2=13|6&IC2=0&DP=4312&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13&TT=1&TTM=1&PID=PMI14448&DPR=FISCHER%20ATCOM"
driver.get(URL_detail)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)

##find cena detail, all
detailCenaAll = driver.find_element_by_xpath("//*[@class='f_column-item']//*[@class='f_price']")
detailCenaAllString = detailCenaAll.text
print("CENA NA DETAILU V SEDIVCE:  ")
print(detailCenaAllString)

##proklik do kosiku
time.sleep(15)
mamZajemDetailXpath = "//*[@class='f_section-content'] //*[@class='f_button f_button--important f_set--fullWidth']"
mamZajemDetailElement = driver.find_element_by_xpath(mamZajemDetailXpath)
mamZajemDetailElement.click()

##tento locator alokuje 2x elementy ktere se sami sobe rovnaji
kosikCenaAllXpath = "//*[@class='f_box f_box--price']//*[@class='f_price']"
kosikCenaAllElement = driver.find_element_by_xpath(kosikCenaAllXpath)
kosikCenaAllString = kosikCenaAllElement.text
print("             ")
print("CENA V KOSIKU:")
print(kosikCenaAllString)

if kosikCenaAllString != detailCenaAllString:
    print(URL_detail)

assert kosikCenaAllString == detailCenaAllString