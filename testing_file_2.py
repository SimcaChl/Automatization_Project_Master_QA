import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://www.fischer.cz/spanelsko/fuerteventura/morro-jable/blue-sea-jandia-luz?AC1=2&D=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&DD=2023-02-19&DP=4312&DPR=FISCHER+ATCOM&DS=256&GIATA=32289&HID=1629&IC1=0&KC1=0&MNN=7&MT=6&NN=7&PID=FUE90003&RD=2023-02-26&TO=4312|4305|2682|4308&acm1=2&df=2023-02-01|2023-03-31&nnm=7|8|9|10|11|12|13&sortby=Departure&tom=4312|4305|2682|4308&tt=1&ttm=1#/terminy-a-ceny"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(15)

boxTerminyXpath = "//*[@class='f_holder']"
boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
time.sleep(4)


celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
celkovaCenaSorterElement.click()
time.sleep(20)

##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

##elemenet vypada jako "41 276 Kč"
##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
"38 764 Kč"


pocetTerminuXpath = "//*[@class='f_termList-header-item']"
pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
poziceTerminu = 0
for _ in pocetTerminuElements:

    celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 xlg:pl-0']"
    celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
    kcIndex = 2
    celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
    celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
    poziceTerminu = poziceTerminu+1
    print(celkovaCenaVterminechINT)

def price_sorter_expensive_cheap (inputList, typeOfSort):

    if typeOfSort == "cheap":
        inputListSorted = inputList.sort()  ##sorting second list low to high

        if cenaZajezduAllListSorted == cenaZajezduAllList:  ##compare first list to second list, if is equal = good
            print("Cheap sorter is OK")

        else:
            print("Cheap sorter is NOT OK")

    if typeOfSort == "expensive":
        cenaZajezduAllListSorted.sort(reverse=True)

        if cenaZajezduAllListSorted == cenaZajezduAllList:
            print("Expensive sorter is OK")

        else:
            print("Expensive sorter is NOT OK")

    print("LIST FROM WEB:")
    print(cenaZajezduAllList)
    print("CORRECTLY SORTED LIST")
    print(cenaZajezduAllListSorted)

    assert cenaZajezduAllListSorted == cenaZajezduAllList