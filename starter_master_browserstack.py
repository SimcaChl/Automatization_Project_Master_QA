from FW_Automation_Local_Deploy_PyCharm.starter_local import *
from EW_Automation_Local_Deploy_PyCharm.starter_local import *
from ET_Automation_Local_Deploy_PyCharm.starter_local import *
from FW_Automation_Local_Deploy_PyCharm.starter_local import *
import unittest

import HtmlTestRunner
#import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)
def runner_tests_generalized(suite_general):
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title=suite_general,
                                           report_name=suite_general,
def running_suites_over_and_over_EW():

        print("EW suite")
        runner_tests_generalized(EW_full_suite)
        print("EW suite should be done")
        time.sleep(20)

def running_suites_over_and_over_FW():

        print("FW suite")
        runner_tests_generalized(FW_full_suite)
        print("FW suite should be done")
        time.sleep(20)


def running_suites_over_and_over_BIG():
    runner_tests_generalized(FW_full_suite), runner_tests_generalized(EW_full_suite)

running_suites_over_and_over_BIG()
#EW_full_suite()
#FW_full_suite()
#ET_full_suite()
#runner_tests_generalized(ET_full_suite)