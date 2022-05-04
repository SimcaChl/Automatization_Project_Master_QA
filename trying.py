brand_name = "ETRAVEL"

desired_cap = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : brand_name,
"build" : "buid",
"name" : "name",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"
}

def desired_cap_Branded(brand_name):
    print (desired_cap)
    return(desired_cap)

desired_cap_Branded()