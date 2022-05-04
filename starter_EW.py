from starter_master_browserstack import *
from EW_Automation_Local_Deploy_PyCharm.starter_local import *
from EW_Automation_Local_Deploy_PyCharm import *
#runner_tests_generalized(EW_full_suite())

#C:\Users\KDK\Desktop\Automatization_Project_Master\starter_FW.py
brand_name = "EXIM"
desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : {brand_name},
"build" : "buid",
"name" : "name",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"
}

runner_tests_generalized(suite_EW_full, "EW")
