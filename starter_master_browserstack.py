#from FW_Automation_Local_Deploy_PyCharm.starter_local import suite
from Automatization_Project_Master.FW_Automation_Local_Deploy_PyCharm import *
from Automatization_Project_Master.FW_Automation_Local_Deploy_PyCharm import *


import unittest

import HtmlTestRunner

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #outfile = open("C:\Users\KDK\Desktop\HTML_TEST_REPORTS\sest_results.html", "w")
    outfile = open("results.html", "w")

    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report',
                            open_in_browser=True, description="FISCHER WEB Suite Report")
    #runner = HTMLTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report', open_in_browser=True, description="FISCHER WEB Suite Report")
    ##at office PC gotta be set up like that (???)
    runner.run(suite())