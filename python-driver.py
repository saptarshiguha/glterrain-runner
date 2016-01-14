from __future__ import print_function

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import calendar
import time
import os, sys

## Change this.
## numiter is 25 to match talos, though I have kept 50
## filename is where the output is kept
## Note here, firefox is started once and the page is reloaded multiple times
## Another approach would be to restart Firefox each time

numiter = 1
filename = "/tmp/glterrain-result-"+str(calendar.timegm(time.gmtime()))+".json"


perffile="file://"+os.path.abspath("./perftest.html")

#binary = FirefoxBinary("/Applications/FirefoxNightly.app/Contents/MacOS/firefox")

driver = webdriver.Firefox() #firefox_binary=binary)
f = open(filename, "w")
try:
    for x in range(0,numiter):
        print(str(x)+" trial")
        driver.get(perffile)
        WebDriverWait(driver, 30*60).until(EC.title_contains("DONE"))
    script = 'return localStorage.getItem("glTerrainJSONData") ;'
    result = driver.execute_script(script)
    print(result, file=f)
finally:
    driver.quit()
    f.close()

