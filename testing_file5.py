import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent
from selenium.common.exceptions import NoSuchElementException

sedivkaXpathFw = "//*[@class='f_box h-full flex flex-col']"

driver = webdriver.Chrome(ChromeDriverManager().install())
#URL = "https://exim.stg.dtweb.cz/poznavaci-zajezdy"
#URL = "https://www.fischer.cz/turecko/istanbul-a-okoli/istanbul/istanbul-mesto-dvou-kontinentu?KEY=0xE027843503B18C35BA3AFE09B421244CCAED2E61&DS=1&HID=90395&MT=1&DI=49&RT=15&NN=3&DF=2022-11-08|2024-05-08&RD=2022-12-11&DD=2022-12-08&ERM=0&AC1=2&KC1=0&IC1=0&DP=4312&MNN=3&NNM=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24&TT=1&TTM=0&PID=ISTVIK&DPR=Fischer"
URL = "https://www.fischer.cz/recko/korfu/roda/angela-beach?DS=256&GIATA=632&D=1225|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|826|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&HID=145146&MT=5&NN=7&DF=2023-07-01|2023-08-31&RD=2023-08-31&DD=2023-08-24&ERM=0&AC1=2&KC1=0&IC1=0&DP=4305&TO=4312|4305|2682|4308&TOM=4312|4305|2682|4308&MNN=7&NNM=7|8|9|10|11|12|13|14|15&TT=1&TTM=1&PID=CFU50152&DPR=FISCHER%20ATCOM"
#URL = "https://fischer.web1.dtweb.cz/"
driver.get(URL)
time.sleep(1)
driver.maximize_window()
acceptConsent(driver)
time.sleep(10)
try:
    sedivka = driver.find_element_by_xpath(sedivkaXpathFw)
    print(sedivka.is_displayed())
    assert 1==1
except NoSuchElementException:
    print("sedivka nenalezena")
    assert 1==2

# sedivka = driver.find_element_by_xpath(sedivkaXpathFw)
# print(sedivka.is_displayed())