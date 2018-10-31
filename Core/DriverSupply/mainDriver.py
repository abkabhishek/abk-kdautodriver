
import time
from sys import stdout as console

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import Core.DriverSupply.common as COM

class KeyDriver:

    def __init__(self,driver):
        self.driver = driver

    def get(self,name,*args):
        return getattr(self.driver,name,*args)

    def run(self,name,*args):
        obj = getattr(self.driver,name)
        return obj(*args)

    def find(self,optionKey,optionValue):
        return COM.FindElem(self.driver,self._selectLocator(optionKey),optionValue)

    def _selectLocator(self,optionKey):
        console.write("Matching Selector")
        if optionKey == "ID":
            return By.ID
        elif optionKey == "XPATH":
            return By.XPATH
        elif optionKey =="LINK_TEXT":
            return By.LINK_TEXT
        elif optionKey == "PARTIAL_LINK_TEXT":
            return By.PARTIAL_LINK_TEXT
        elif optionKey == "NAME":
            return By.NAME
        elif optionKey == "TAG_NAME":
            return By.TAG_NAME
        elif optionKey == "CLASS_NAME":
            return By.CLASS_NAME
        elif optionKey == "CSS_SELECTOR":
            return By.CSS_SELECTOR
        else:
            console.write("Invalid selector")
            return False




class KeyElement:


    def get(self,element,name, *args):
        return getattr(element,name,*args)

    def run(self,element,name,*args):
        obj = getattr(element,name)
        x = obj(*args)
        return x







class MainDriver:


    def __init__(self,driver):
        MainDriver.driver = driver
        self.K = KeyDriver(driver)
        self.E = KeyElement()

    def rowReader(self,row):
        parameters=[]
        for parameter in row[5:]:
            if parameter != '':
                parameters.append(parameter)
        if row[1]=="E":
            self.K.run(row[0],*parameters)
            return True
        elif row[1]=="G":
            setattr(self,row[2],self.K.get(row[0],*parameters))
            return True
        elif row[1]=="GV":
            assert row[3] in self.K.get(row[0],*parameters)
            return True
        elif row[0]=="find_element":
            result = self.K.find(*parameters)
            if result:
                setattr(self, row[2], result)
                return True
            else:
                console.write("Element not found")
                setattr(self, row[2], None)
                return False
        elif row[1]=="ES-E":
            setattr(self, row[2], self.K.run(row[0],By.NAME,*parameters[1:]))
            return True
        elif row[1]=="EG-E":
            if getattr(self,row[2]) != None:
                self.E.run(getattr(self,row[2]),row[0],*parameters)
                return True
            else:
                console.write("Element not present")
                return False




