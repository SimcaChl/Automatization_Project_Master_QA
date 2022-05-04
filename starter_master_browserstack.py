from KTGSK_Automation_Local_Deploy_PyCharm import *
import unittest

import HtmlTestRunner
#import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)
def runner_tests_generalized(suite_general, web_brand):
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title=web_brand,
                                           report_name=web_brand+' WEB Suite Report',
                                           open_in_browser=True, description=web_brand+" WEB Suite Report")
    runner.run(suite_general())


