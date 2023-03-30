from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import time
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
producturl="https://www.amazon.in/Tecno-Spark-Infinity-Expandable-Processor/dp/B0B56YZT37/ref=sr_1_1_sspa?crid=1LWWHQB3R5I2B&keywords=smartphones&qid=1676318496&sprefix=smartphones%2Caps%2C396&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
driver.get(producturl)
driver.find_element(By.XPATH, "(//input[@id='add-to-cart-button'])[1]").click()