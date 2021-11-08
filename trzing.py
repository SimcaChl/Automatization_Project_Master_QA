
def osloveniLocators(pocetCestujicich):
    locator = "(//*[@class='f_input-optionsWrapper js_optionsWrapper'] //*[@class='f_input-option-text'])"
    osloveniLocatorsList = []
    pocetCestujicich = pocetCestujicich*2
    for _ in range(pocetCestujicich):

        correctLocator = locator + "[" + str(pocetCestujicich) + "]"
        ##print(correctLocator)

        osloveniLocatorsList.append(correctLocator)
        pocetCestujicich = pocetCestujicich - 1

    ##print(osloveniLocatorsList)
    return(osloveniLocatorsList)

osloveniLocators(2)

print(osloveniLocators(2)[3])