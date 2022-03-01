import unittest
from CovidInfo_D import *
from pobocky import *
from Detail_D import *
from Detail_C import *
from DetskeKluby_D import *
from dovolena_D import *
from FM_D import *
from fulltext_C import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPobocky_D('test_pobocky_D'))
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
    suite.addTest(Test_Fulltext_C("TestFMexotika_D"))




    return suite

if __name__ == '__main__':

    #runner = unittest.TextTestRunner()
    runner = unittest.TestRunner()
    runner.run(suite())