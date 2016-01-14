from __future__ import print_function

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import calendar
import time


binary = FirefoxBinary("/Applications/FirefoxNightly.app/Contents/MacOS/firefox")
driver = webdriver.Firefox() #firefox_binary=binary)

numiter = 25
filename = "/tmp/glterrain-result-"+str(calendar.timegm(time.gmtime()))+".json"
f = open(filename, "w")
try:
    for x in range(0,numiter):
        print(str(x)+" trial")
        driver.get("file:///Users/sguha/mz/misc/glterrain-runner/perftest.html")
        WebDriverWait(driver, 30*60).until(EC.title_contains("DONE"))
    script = 'return localStorage.getItem("glTerrainJSONData") ;'
    result = driver.execute_script(script)
    print(result, file=f)
finally:
    driver.quit()
    f.close()

