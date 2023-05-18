from FWSK_Automation_Local_Deploy_PyCharm.to_import import URL, setUp, tearDown
import unittest

from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://fischer.sk"

URL_SRL_FWSK1 = "/vysledky-vyhladavania?ac1=2&d=958|664&dd=2023-09-01&ka1=5|2&kc1=2&nn=7|8|9|10|11|12|13&rd=2023-10-01&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK2 = "/vysledky-vyhladavania?ac1=2&d=687|654|604&dd=2023-09-01&ka1=5|2&kc1=2&nn=7|8|9|10|11|12|13&rd=2023-10-01&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK3 = "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-01&ka1=5|2&kc1=2&nn=4|5|6|7|8|9|10|11|12|13&rd=2023-11-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK4 = "/vysledky-vyhladavania?ac1=2&d=618|619|624|973|595|746|1225|623|741|735|993|648|972|620&dd=2023-09-01&nn=4|5|6|7|8|9|10|11|12|13&rd=2023-10-31&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK5 = "/vysledky-vyhladavania?ac1=2&d=1111&dd=2023-08-01&ka1=7&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-09-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK6 = "/vysledky-vyhladavania?ac1=2&d=664&dd=2023-11-01&ds=0&ifm=0&ilm=0&ka1=7&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-12-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK7 = "/vysledky-vyhladavania?ac1=2&d=664&dd=2023-11-01&ds=0&ic1=1&ifm=0&ilm=0&ka1=7&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-12-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK8 = "/vysledky-vyhladavania?ac1=2&d=627|974|712|684|955|596&dd=2023-10-01&ds=0&ifm=0&ilm=0&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-11-30&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK9 = "/vysledky-vyhladavania?ac1=2&d=653|819|724&dd=2023-10-01&ic1=1&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-11-30&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK10 = "/vysledky-vyhladavania?ac1=2&d=593&dd=2023-10-01&ds=0&ifm=0&ilm=0&ka1=10&kc1=1&nn=7|8|9|10|11|12|13&rd=2023-11-30&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK11 = "/vysledky-vyhladavania?ac1=2&d=621|1009|680|622|1108|953|669|1086|978|594|611|610|592|675|612|1010|590|726|683|609&dd=2023-09-01&ds=0&ifm=0&ilm=0&nn=5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRL_FWSK12 = "/vysledky-vyhladavania?ac1=2&d=1005&dd=2023-09-01&ds=0&ifm=0&ilm=0&nn=5|6|7|8|9|10|11|12|13&rd=2023-10-31&sc=residential&to=483|1837|2933|3437&tt=1"

URL_SRLs_list_FWSK = [URL_SRL_FWSK1, URL_SRL_FWSK2, URL_SRL_FWSK3, URL_SRL_FWSK4, URL_SRL_FWSK5, URL_SRL_FWSK6, URL_SRL_FWSK7, URL_SRL_FWSK8, URL_SRL_FWSK9, URL_SRL_FWSK10, URL_SRL_FWSK11, URL_SRL_FWSK12]



class Test_SRL_C_comparer(unittest.TestCase):
    def setUp(self):
        setUp(self)


    def tearDown(self):
        tearDown(self)


    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, URL, URL_public_prod, URL_SRLs_list_FWSK)



        self.test_passed = True