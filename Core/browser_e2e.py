import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class KeyDriver:

    def __init__(self,driver):
        self.driver = driver

    def get(self,name,*args):
        return getattr(self.driver,name,*args)

    def run(self,name,*args):
        obj = getattr(self.driver,name)
        return obj(*args)




class KeyElement:


    def get(self,element,name, *args):
        return getattr(element,name,*args)

    def run(self,element,name,*args):
        obj = getattr(element,name)
        x = obj(*args)
        return x





def main():
    options = webdriver.ChromeOptions()
    # if headless:
    #     options.add_argument('--headless')
    options.add_argument("--kiosk")
    driver=webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(2)


    K = KeyDriver(driver)
    E = KeyElement()

    K.run("get","https://www.google.com")

    assert "Google" in K.get("title")

    elem = K.run("find_element",By.NAME, "q")

    E.run(elem,"send_keys","paris")



    time.sleep(3)

    driver.quit()