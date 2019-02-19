import traceback
import time
import unittest
from sys import stdout as console

from selenium import webdriver

from Core.Services.fileReader import *
from Core.DriverSupply.mainDriver import *

def main(myFile):

    FL = FLRead(myFile).FL

    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    driver=webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(2)

    E = MainDriver(driver)

    for row in FL:
        try:
            assert E.rowReader(row)
        except AssertionError as e:
            print(traceback.format_exc())
            continue




    time.sleep(3)

    driver.quit()

