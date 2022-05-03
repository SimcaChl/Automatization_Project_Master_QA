#from FW_Automation_Local_Deploy_PyCharm.starter_local import suite
#from Automatization_Project_Master.FW_Automation_Local_Deploy_PyCharm import *

from os import path
import sys
sys.path.append(path.abspath('/FW_Automation_Local_Deploy_PyCharm'))
#sys.path.append(path.abspath('/EW_Automation_Local_Deploy_PyCharm'))
from FW_Automation_Local_Deploy_PyCharm.starter_local import *
from EW_Automation_Local_Deploy_PyCharm.starter_local import *
from ET_Automation_Local_Deploy_PyCharm.starter_local import *
import unittest

import HtmlTestRunner
#import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)
def FW_full_suite():
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report',
                            open_in_browser=True, description="FISCHER WEB Suite Report")
    runner.run(suite_FW_full())
def EW_full_suite():
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='EXIM WEB Suite Report', report_name='EXIM WEB Suite Report',
                            open_in_browser=True, description="EXIM WEB Suite Report")
    runner.run(suite_EW_full())

def ET_full_suite():
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='EXIM WEB Suite Report', report_name='EXIM WEB Suite Report',
                            open_in_browser=True, description="EXIM WEB Suite Report")
    runner.run(suite_ET_full())

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
#FW_full_suite()
ET_full_suite()