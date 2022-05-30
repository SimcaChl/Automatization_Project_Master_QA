from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from ET_Automation_Local_Deploy_PyCharm.to_import import acceptConsent

Rekapitulace_ZaplatitNyniXpath = "//*[@class='box box--invisible forDesktop']//*[@class='list-item']/a"

Doplatek_ZaplatitButtonXpath = "//*[@class='f_button f_button--important']"
Doplatek_AmountToPayBoxXpath = "//*[@name='amount']"
Doplatek_CanceledStatusBackToPaymentXpath = "//*[@class='fshr-paragraph--centered']/a"


PaymentGateway_CSOBczCardPaymentBackToShopXpath = "//*[@class='button-with-icon button-cancel']"
PaymentGateway_CSOBczCardPaymentTotalPrice = "//*[@class='total-price']"  ##result = 123,00 CZK
                                                                            ##vzit jen prvni 4cislice?
URL = "https://www.eximtours.cz/objednavka/objednavka-zajezdu-rekapitulace?hash=588b8483-2eae-48d4-bf96-04b0fa0edba6"
driver = webdriver.Chrome(ChromeDriverManager().install())
amountToPay = "9696"
def rekapitulace_proklik_doplatek(driver, URL_rekapitulace):


    driver.maximize_window()
    driver.get(URL_rekapitulace)
    time.sleep(2)
    acceptConsent(driver)
    driver.find_element_by_xpath(Rekapitulace_ZaplatitNyniXpath).click()
##after execution of above im at doplatek

rekapitulace_proklik_doplatek(driver, URL)
time.sleep(5)
Doplatek_AmountToPayBoxElement = driver.find_element_by_xpath(Doplatek_AmountToPayBoxXpath)
Doplatek_AmountToPayBoxElement.clear()
time.sleep(0.5)
Doplatek_AmountToPayBoxElement.send_keys(amountToPay)
time.sleep(2)
driver.find_element_by_xpath(Doplatek_ZaplatitButtonXpath).click()
time.sleep(3)


driver.find_element_by_xpath(PaymentGateway_CSOBczCardPaymentBackToShopXpath).click()
time.sleep(3)

driver.find_element_by_xpath(Doplatek_CanceledStatusBackToPaymentXpath).click()