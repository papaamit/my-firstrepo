from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()

mobiles = driver.find_element(By.XPATH, "(//a[normalize-space()='Mobiles'])[1]").click()
smartphones = driver.find_element(By.XPATH, "(//a[normalize-space()='Smartphones'])[1]").click()
buttons = driver.find_element(By.XPATH, "(//img[@alt='Shop now'])[1]").click()
add_to_button = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

laptops = driver.find_element(By.XPATH, "(//span[normalize-space()='Laptops & Accessories'])[1]")
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
tablets = driver.find_element(By.XPATH, "//div[15]//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()

lenovo = driver.find_element(By.XPATH, "(//span[contains(text(),'Lenovo Tab M10 FHD Plus (3rd Gen) (10.61 inch (26.')])[1]").click()
