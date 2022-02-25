from poznavacky import TestPoznavacky_D
from threading import Thread
from to_import_secret import comandExecutor


from to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky
cap=[{
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      }]
#Thread(target=TestPoznavacky_D)
Thread(target=TestPoznavacky_D, args=(cap,)).start()