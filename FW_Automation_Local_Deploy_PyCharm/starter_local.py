from FW_Automation_Local_Deploy_PyCharm.CovidInfo_D import *
from FW_Automation_Local_Deploy_PyCharm.pobocky import *
from FW_Automation_Local_Deploy_PyCharm.Detail_D import *
from FW_Automation_Local_Deploy_PyCharm.Detail_C import *
from FW_Automation_Local_Deploy_PyCharm.DetskeKluby_D import *
from FW_Automation_Local_Deploy_PyCharm.dovolena_D import *
from FW_Automation_Local_Deploy_PyCharm.FM_D import *
from FW_Automation_Local_Deploy_PyCharm.fulltext_C import *
from FW_Automation_Local_Deploy_PyCharm.groupsearch_D import *
from FW_Automation_Local_Deploy_PyCharm.HP_D import *
from FW_Automation_Local_Deploy_PyCharm.LM_D import *
from FW_Automation_Local_Deploy_PyCharm.poznavacky import *
from FW_Automation_Local_Deploy_PyCharm.SDO_D import *
from FW_Automation_Local_Deploy_PyCharm.SRL_C import *
from FW_Automation_Local_Deploy_PyCharm.SRL_D import *
from FW_Automation_Local_Deploy_PyCharm.HP_C import *
import HtmlTestRunner
import HTMLTestRunner   as   HtmlTestRunner  ##at office PC gotta be set up like that (???)

def suite_FW_full():
    suite = unittest.TestSuite()
    suite.addTest(TestCovidInfo_D('test_covidInfo_D'))
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(TestDetskeKluby_D("test_kluby_D"))
    suite.addTest(TestDovolena_D("test_dovolena_D"))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_lM_isDisplayed"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D'))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    #suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

def suite_map():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    return suite

def suite_HP_bannery():
    suite = unittest.TestSuite()
    suite.addTest(Test_HP_C('test_HP_bannery_check'))
    return suite

from starter_master_browserstack import  runner_tests_generalized
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report',
                            open_in_browser=True, description="FISCHER WEB Suite Report- WEB1")

    web_brand = "FISCHER"
    runner_tests_generalized(suite_FW_full, web_brand, "hotifx", URL)
    #runner_tests_generalized(suite_HP_bannery, web_brand, "hotifx", URL)