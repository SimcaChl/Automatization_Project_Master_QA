import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

##open SRLS , take h1, compare pocet vysledku VS dev ENV
from random_printer import checked_URLs_list

driver = webdriver.Chrome(ChromeDriverManager().install())
URL_prod = "https://www.fischer.cz/"
URL_dev = "https://fischer.web2.dtweb.cz/"
#URL_dev = "https://fischer.web3.dtweb.cz/"
# URL1 = URL+ "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2022-12-01&nn=7&rd=2023-01-31&to=4312|4305|2682|4308&tt=1"
# URL2 = URL+ "vysledky-vyhledavani?ac1=2&d=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL3 = URL+ "vysledky-vyhledavani?ac1=2&d=1006|1007|1008&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL4 = URL+ "vysledky-vyhledavani?ac1=2&d=664&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL5 = URL+ "vysledky-vyhledavani?ac1=2&d=756&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL6 = URL+ "vysledky-vyhledavani?ac1=2&d=661&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL7 = URL+ "vysledky-vyhledavani?ac1=2&d=1111&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
# URL8 = URL+ "vysledky-vyhledavani?ac1=2&d=790&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL9 = URL+ "vysledky-vyhledavani?ac1=2&d=633|994&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL10 = URL+ "vysledky-vyhledavani?ac1=2&d=634&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL11 = URL+ "vysledky-vyhledavani?ac1=2&d=631&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL12 = URL+ "vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
# URL13 = URL+ "vysledky-vyhledavani?ac1=2&d=638&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"

URL1 = "vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2022-12-01&nn=7&rd=2023-01-31&to=4312|4305|2682|4308&tt=1"
URL2 = "vysledky-vyhledavani?ac1=2&d=680|953|1108|592|611|610|612|590|726|609|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL3 = "vysledky-vyhledavani?ac1=2&d=1006|1007|1008&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL4 = "vysledky-vyhledavani?ac1=2&d=664&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL5 =  "vysledky-vyhledavani?ac1=2&d=756&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL6 = "vysledky-vyhledavani?ac1=2&d=661&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL7 = "vysledky-vyhledavani?ac1=2&d=1111&dd=2023-02-01&ds=0&nn=7&rd=2023-03-28&to=4312|4305|2682|4308&tt=1"
URL8 =  "vysledky-vyhledavani?ac1=2&d=790&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL9 ="vysledky-vyhledavani?ac1=2&d=633|994&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL10 = "vysledky-vyhledavani?ac1=2&d=634&dd=2023-01-01&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL11 = "vysledky-vyhledavani?ac1=2&d=631&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL12 ="vysledky-vyhledavani?ac1=2&d=751&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL13 =  "vysledky-vyhledavani?ac1=2&d=638&dd=2023-01-01&ds=0&nn=7|8|9|10|11|12|13&rd=2023-02-28&to=4312|4305|2682|4308&tt=1"
URL14 = "vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1"

####
URL15 = "vysledky-vyhledavani?ac1=2&d=958|664|687|604|1005|1008|1007|653|819|724|634|756|751|605|677|680|1108|953|611|610|592|612|590|726|609|1066|1006|745|1061|965|822|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-07-01&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL16 = "vysledky-vyhledavani?ac1=2&d=958|664|687|604|1005|1008|1007|653|819|724|634|756|751|605|677|680|1108|953|611|610|592|612|590|726|609|790|607|591|627|974|712|596|1066|1006|745|1061|965|822|621|1009|622|669|1086|1194|670|978|594|675|1010|683|636|950|980|945|951|947|946&dd=2023-07-01&ka1=12|4&kc1=2&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL17 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=860|1050|1039|859|875|1043|1044|1057&dd=2022-12-22&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=1|2|3|4|5|6|7|8|9|10|11|12&rd=2023-02-21&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL18 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=1182|1190|1184|1183|1178&dd=2022-12-22&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=1|2|3|4|5|6|7|8|9|10|11|12&rd=2023-02-21&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL19 = "dovolena-na-horach/vysledky-vyhledavani?ac1=2&d=1051&dd=2023-08-01&ds=0&ea=356&ifm=0&ilm=0&ka1=12&kc1=1&nn=7|8|9&rd=2023-09-30&sc=skiing&to=4312|4305|2682|4308&tt=3"
URL20 = "vysledky-vyhledavani?ac1=3&d=664|687|604|1225|623|741|735|618|619|624|973|993|595|648|972|620|746|680|1108|953|611|610|592|612|590|726|609|607|591|627|974|712|596|621|1009|622|669|1086|1194|670|978|594|675|1010|683&dd=2023-04-01&ic1=1&ka1=11&kc1=1&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL21 = "vysledky-vyhledavani?ac1=3&d=1008|1007|1111|661|605|677|1225|623|741|735|618|619|624|973|993|595|648|972|620|746|1066|1006|745|1061|965|822|636|950|980|945|951|947|946&dd=2023-04-01&ic1=1&ka1=11&kc1=1&nn=7|8|9&rd=2023-08-31&to=4312|4305|2682|4308&tt=1"
URL22 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=626|957|589&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"
URL23 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=608&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"
URL24 = "poznavaci-zajezdy/vysledky-vyhledavani?ac1=2&d=1133|606|860|870|1098|770|1050|1134|823|1039|1109|644|643|674|871|1172|805|875|791|815|1040|1041|869|629|642|1078|616|859|1079|962|1042|1043|1044|1045|1057&dd=2022-12-22&ds=0&ea=518&ifm=0&ilm=0&nn=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20&rd=2023-12-31&sc=sightseeing&to=4312|4305|2682|4308&tt=0"

URL_List = [URL1,URL2, URL3, URL4, URL5,URL6, URL7,URL8,URL9,URL10,URL11,URL12,URL13, URL14, URL15, URL16, URL17, URL18, URL19, URL20, URL21, URL22, URL23, URL24]
#URL_List = [URL1,URL2]

def list_SRL_number_of_results(driver, URL_default, URL_dev ,URL_parameters_list):
    driver.get(URL_default)
    time.sleep(1)
    driver.maximize_window()
    acceptConsent(driver)
    time.sleep(5)
    windowHandle = 1
    listPosition = 0

    ##default pocitejme jako PROD

    global pocet_vysledku_list_default
    pocet_vysledku_list_default = []


    global checked_URLs_list_default
    checked_URLs_list_default = []

    global pocet_vysledku_list_dev
    pocet_vysledku_list_dev = []

    global checked_URLs_list_dev
    checked_URLs_list_dev = []



    for _ in URL_List:
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[windowHandle])
        linkActualUrl = URL_default + URL_parameters_list[listPosition]
        time.sleep(3)
        driver.get(linkActualUrl)
        SRL_H1textPocetNalezenychZajezduXpath = "//h1"

        pocetNalezenychZajezduElement = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        pocet_vysledku_list_default.append(pocetNalezenychZajezduElement)

        checked_URLs_list_default.append(linkActualUrl)

        #print(pocetNalezenychZajezduElement)
        #print(linkActualUrl)
        windowHandle = windowHandle + 1
        listPosition = listPosition + 1

    windowHandle = 1
    listPosition = 0
    for _ in URL_List:
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[windowHandle])
        linkActualUrl = URL_dev + URL_parameters_list[listPosition]
        #driver.get(URL_dev + "/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
        time.sleep(3)
        driver.get(linkActualUrl)
        SRL_H1textPocetNalezenychZajezduXpath = "//h1"

        pocetNalezenychZajezduElement = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
        pocet_vysledku_list_dev.append(pocetNalezenychZajezduElement)

        checked_URLs_list_dev.append(linkActualUrl)

        #print(pocetNalezenychZajezduElement)
        #print(linkActualUrl)
        windowHandle = windowHandle + 1
        listPosition = listPosition + 1

    starterPosition = 0
    for _ in pocet_vysledku_list_default:
        if pocet_vysledku_list_default[starterPosition] == pocet_vysledku_list_dev[starterPosition]:
            starterPosition=starterPosition+1
            print(pocet_vysledku_list_default[starterPosition])
            print(pocet_vysledku_list_dev[starterPosition])
            print(checked_URLs_list_default[starterPosition])
            print(checked_URLs_list_dev[starterPosition])
            print("             ")
            pass
        if pocet_vysledku_list_default[starterPosition] != pocet_vysledku_list_dev[starterPosition]:
            print(pocet_vysledku_list_default[starterPosition])
            print(pocet_vysledku_list_dev[starterPosition])
            print(checked_URLs_list_default[starterPosition])
            print(checked_URLs_list_dev[starterPosition])
            print("             ")
            starterPosition = starterPosition + 1

        print(starterPosition)

    print(len(pocet_vysledku_list_default))


#list_SRL_number_of_results(driver, URL_prod, URL_dev ,URL_List)














































# windowHandle = 1
# listPosition = 0
# for _ in URL_List:
#     driver.execute_script("window.open("");")
#     driver.switch_to.window(driver.window_handles[windowHandle])
#     linkActualUrl = URL_List[listPosition]
#     driver.get(URL+"/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
#     time.sleep(3)
#     driver.get(linkActualUrl)
#     SRL_H1textPocetNalezenychZajezduXpath = "//h1"
#     pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
#     print(pocetNalezenychZajezduElement_PROD)
#     print(linkActualUrl)
#     windowHandle = windowHandle + 1
#     listPosition = listPosition + 1
#
# for _ in URL_List:
#     driver.execute_script("window.open("");")
#     driver.switch_to.window(driver.window_handles[windowHandle])
#     linkActualUrl = URL_List[listPosition]
#     driver.get(URL_dev+"/vysledky-vyhledavani?ac1=2&d=680%7C953%7C1108%7C592%7C611%7C610%7C612%7C590%7C726%7C609%7C621%7C1009%7C622%7C669%7C1086%7C1194%7C670%7C978%7C594%7C675%7C1010%7C683&dd=2023-02-01&nn=7&rd=2023-03-28&to=4312%7C4305%7C2682%7C4308&tt=1")
#     time.sleep(3)
#     driver.get(linkActualUrl)
#     SRL_H1textPocetNalezenychZajezduXpath = "//h1"
#     pocetNalezenychZajezduElement_DEV = driver.find_element_by_xpath(SRL_H1textPocetNalezenychZajezduXpath).text.lower()
#     print(pocetNalezenychZajezduElement_DEV)
#     print(linkActualUrl)
#     windowHandle = windowHandle + 1
#     listPosition = listPosition + 1