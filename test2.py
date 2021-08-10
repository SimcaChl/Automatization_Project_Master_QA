from VARIABLES import *
from FUNCTIONS import *

driver.get(URL)
time.sleep(10)

##advanced = driver.find_element_by_xpath("/html/body/div[15]//section/div/div[2]")
##wait.until(EC.visibility_of(advanced))
##advanced.click()
accpet = driver.find_element_by_xpath("//*[@data-testid='uc-accept-all-button']")
wait.until(EC.visibility_of(accpet))
##proceed = driver.find_element_by_xpath('/html/body/div[15]//section/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]')
##wait.until(EC.visibility_of(proceed))

##wait.until(EC.visibility_of(proceed))
time.sleep(5)
##proceed.click()
accpet.click()