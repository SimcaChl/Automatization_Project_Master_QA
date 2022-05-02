#from FW_Automation_Local_Deploy_PyCharm.starter_local import suite
#from Automatization_Project_Master.FW_Automation_Local_Deploy_PyCharm import *

from os import path
import sys
sys.path.append(path.abspath('/FW_Automation_Local_Deploy_PyCharm'))
#sys.path.append(path.abspath('/EW_Automation_Local_Deploy_PyCharm'))
from FW_Automation_Local_Deploy_PyCharm.starter_local import *
from EW_Automation_Local_Deploy_PyCharm.starter_local import *
import unittest

import HtmlTestRunner
#import HTMLTestRunner
def FW_full_suite():
#if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #outfile = open("C:\Users\KDK\Desktop\HTML_TEST_REPORTS\sest_results.html", "w")
    outfile = open("results.html", "w")

    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report',
                            open_in_browser=True, description="FISCHER WEB Suite Report")
    #runner = HTMLTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report', open_in_browser=True, description="FISCHER WEB Suite Report")
    ##at office PC gotta be set up like that (???)
    runner.run(suite_FW_full())
def EW_full_suite():
#if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #outfile = open("C:\Users\KDK\Desktop\HTML_TEST_REPORTS\sest_results.html", "w")
    outfile = open("results.html", "w")

    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='EXIM WEB Suite Report', report_name='EXIM WEB Suite Report',
                            open_in_browser=True, description="EXIM WEB Suite Report")
    #runner = HTMLTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report', open_in_browser=True, description="FISCHER WEB Suite Report")
    ##at office PC gotta be set up like that (???)
    runner.run(suite_EW_full())

def running_suites_over_and_over():
    while True:
        print("EW suite")
        EW_full_suite()

        time.sleep(900)
        print("FW suite")
        FW_full_suite()

        time.sleep(426)
#running_suites_over_and_over()
#EW_full_suite()
FW_full_suite()