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
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report',
                                           report_name='FISCHER WEB Suite Report',
                                           open_in_browser=True, description="FISCHER WEB Suite Report")
    runner.run(suite_general())
from threading import Thread
import runpy
Thread(target=runpy.run_path(path_name='starter_FW.py'), args=(cap,)).start()
print("thread")
time.sleep(2)

Thread2(target=runpy.run_path(path_name='starter_EW.py'), args=(cap,)).start()
