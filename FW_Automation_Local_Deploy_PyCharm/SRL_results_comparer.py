from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FW_Automation_Local_Deploy_PyCharm.to_import import URL, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://fischer.cz"
URL_SRL_FW1 = "/vysledky-vyhledavani?ac1=2&d=621|1009|680|622|1108|953|669|1086|1194|670|978|594|611|610|592|675|612|1010|590|726|683|609&dd=2023-09-01&ds=0&ic1=1&ifm=0&ilm=0&nn=7|8|9|10|11|12|13&rd=2023-09-30&sc=residential&to=4312|4305|2682|4308&tt=1"

URL_SRL_FW2 = "/vysledky-vyhledavani?ac1=2&d=1225|623|741|735|618|619|624|973|993|595|648|972|620|746&dd=2023-09-01&ic1=2&nn=7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308&tt=1"

URL_SRL_FW3 = "/vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2023-10-01&nn=7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW4 = "/vysledky-vyhledavani?ac1=2&d=650|651|649|876&dd=2023-10-01&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW5 = "/vysledky-vyhledavani?ac1=2&d=644|674|642|616|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=2023-09-01&ic1=1&ka1=10&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW6 = "/vysledky-vyhledavani?ac1=2&d=654|634&dd=2023-07-01&ic1=1&ka1=10&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW7 = "/vysledky-vyhledavani?ac1=2&d=607|591&dd=2023-07-01&ic1=1&ka1=10|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW8 = "/vysledky-vyhledavani?ac1=2&d=627|974|712|596&dd=2023-07-01&ic1=1&ka1=10|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW9 = "/vysledky-vyhledavani?ac1=2&d=635&dd=2023-07-01&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-08-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW10 = "/vysledky-vyhledavani?ac1=2&d=605|677|745|1061|965|822&dd=2023-09-01&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW11 = "/vysledky-vyhledavani?ac1=2&d=654&dd=2023-09-01&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW12 = "/vysledky-vyhledavani?ac1=2&d=631&dd=2023-09-01&ic1=1&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW13 = "/vysledky-vyhledavani?ac1=2&d=638|1214|635&dd=2023-10-01&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW14 = "/vysledky-vyhledavani?ac1=2&d=654&dd=2023-10-01&ka1=6&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW15 = "/vysledky-vyhledavani?ac1=2&d=633&dd=2023-10-01&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW16 = "/vysledky-vyhledavani?ac1=2&d=1005&dd=2023-08-01&ka1=15&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW17 = "/vysledky-vyhledavani?ac1=2&d=687|604&dd=2023-08-01&ka1=15|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW18 = "/vysledky-vyhledavani?ac1=2&d=650|651|649|876|644|674|642|616|1133|606|860|870|1098|770|1050|1134|823|1039|1109|643|871|1172|805|875|791|815|1040|1041|869|629|1078|859|1079|962|1042|1043|1044|1045|1057&dd=2023-09-01&ka1=15|6&kc1=2&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-09-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW19 = "/vysledky-vyhledavani?ac1=2&d=653|819|724&dd=2023-09-01&ka1=3&kc1=1&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRL_FW20 = "/vysledky-vyhledavani?ac1=2&d=664&dd=2023-10-01&nn=3|4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=4312|4305|2682|4308|483|1837|2933|3437|3248&tt=1"

URL_SRLs_list_FW = [URL_SRL_FW1, URL_SRL_FW2, URL_SRL_FW3, URL_SRL_FW4, URL_SRL_FW5, URL_SRL_FW6, URL_SRL_FW7, URL_SRL_FW8, URL_SRL_FW9, URL_SRL_FW10, URL_SRL_FW11, URL_SRL_FW12, URL_SRL_FW13, URL_SRL_FW14, URL_SRL_FW15, URL_SRL_FW16, URL_SRL_FW17, URL_SRL_FW18, URL_SRL_FW19, URL_SRL_FW20]


class Test_SRL_C_comparer(unittest.TestCase):
    def setUp(self):
        setUp(self)


    def tearDown(self):
        tearDown(self)


    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, URL, URL_public_prod, URL_SRLs_list_FW)



        self.test_passed = True