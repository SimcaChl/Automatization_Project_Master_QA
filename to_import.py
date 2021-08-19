from selenium.common.exceptions import NoSuchElementException

URL = "https://www.fischer.cz"
URL_faq = URL+"/faq"
URL_stat = URL+"/recko"
URL_lm = URL+"/last-minute"
URL_fm = URL+"/first-minute"
URL_fmExotika = URL+"/first-minute/exotika-zima"


caps=[{
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      }]



def acceptConsent(driver):
    def expand_shadow_element(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    try:
        outer = expand_shadow_element(driver.find_element_by_css_selector("div#usercentrics-root"))
        inner = outer.find_element_by_css_selector("button[data-testid='uc-accept-all-button']")
        inner.click()
    except NoSuchElementException:
        pass