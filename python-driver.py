from __future__ import print_function

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import calendar
import time
import os, sys
import json

## Change this. numiter is 25 to match talos, though I have kept 50 filename is
## where the output is kept Note here, firefox is started once and the page is
## reloaded multiple times Another approach would be to restart Firefox each
## time which is handled here too


numrestart = 1 # Firefox will start this number of times
numiter = 20   # The page will be loaded this number of times
saveData = "/tmp/glterrain-result-"+str(calendar.timegm(time.gmtime()))+".json" # Where to save the data

restarts = []

perffile="file://"+os.path.abspath("./perftest.html")
#binary = FirefoxBinary("/Applications/FirefoxNightly.app/Contents/MacOS/firefox")
for r in range(0, numrestart):
    driver = webdriver.Firefox() #firefox_binary=binary)
    try:
        for x in range(0,numiter):
            print(str(x)+" trial")
            driver.get(perffile)
            WebDriverWait(driver, 30*60).until(EC.title_contains("DONE"))
        script = 'return localStorage.getItem("glTerrainJSONData") ;'
        result = driver.execute_script(script)
        restarts.append(json.loads(result))
    finally:
        driver.quit()

# Write the results to a file
f = open(saveData, "w")
print(json.dumps(restarts), file=f)
f.close()

