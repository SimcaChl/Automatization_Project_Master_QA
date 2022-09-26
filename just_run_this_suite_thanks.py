from starter_master_browserstack import  runner_tests_generalized
from FW_Automation_Local_Deploy_PyCharm.starter_local import *

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    web_brand = "FISCHER"
    version = "pouze   u nas"
    runner_tests_generalized(suite_FW_full, web_brand, version, URL)