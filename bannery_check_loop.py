import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent
import smtplib
from email.mime.text import MIMEText
from to_import_secret_master import emailPass

def sendEmailv2(msg, recipient):
  fromx = 'alertserverproblem@gmail.com'
  to = recipient
  msg = MIMEText(msg)
  msg['Subject'] = "HP CHECK"
  msg['From'] = fromx
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login("alertserverproblem@gmail.com", emailPass)
  server.sendmail(fromx, to, msg.as_string())
  server.quit()


while True:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    URL = "https://www.fischer.cz"
    driver.get(URL)
    time.sleep(1)
    driver.maximize_window()
    acceptConsent(driver)
    time.sleep(15)
    banneryXpath_FW = "//*[@class='f_teaser-item']/a"
    banneryAll = driver.find_elements_by_xpath(banneryXpath_FW)
    SRL_H1textPocetNalezenychZajezduXpath = "//h1"
    x = 0
    pocetNalezenychZajezduElementList_PROD = []
    bannerLinksList_PROD = []
    for _ in banneryAll:
        bannerHref = banneryAll[x].get_attribute("href")
        # print(bannerHref)
        x = x + 1
        # print(x)
        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bannerHref)
        # time.sleep(10)
        try:
            pocetNalezenychZajezduElement_PROD = driver.find_element_by_xpath(
                SRL_H1textPocetNalezenychZajezduXpath).text.lower()
            pocetNalezenychZajezduElementList_PROD.append(pocetNalezenychZajezduElement_PROD)
            bannerLinks_PROD = driver.current_url
            bannerLinksList_PROD.append(bannerLinks_PROD)
            # print (bannerLinks_PROD)
        except NoSuchElementException:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

    print( pocetNalezenychZajezduElementList_PROD)
    print(bannerLinksList_PROD)

    nenasliCoJsteHledaliString = "Nenašli jste, co jste hledali?"


    y = 0
    for _ in pocetNalezenychZajezduElementList_PROD:
        if pocetNalezenychZajezduElementList_PROD[y] == nenasliCoJsteHledaliString:
            print(pocetNalezenychZajezduElementList_PROD[y])
            print("spatny")
            sendEmailv2(bannerLinksList_PROD[y] , "ondrej.kadoun@fischer.cz")

        else:
            print(pocetNalezenychZajezduElementList_PROD[y])
            print("OK")

        y = y + 1

    sendEmailv2("executed FW CHECK HP bannery", "ondrej.kadoun@fischer.cz")
        #sendEmailv2(bannerLinksList_PROD[y], "ondrej.kadoun@fischer.cz")


        #print(y)

    driver.quit()
    time.sleep(3600)