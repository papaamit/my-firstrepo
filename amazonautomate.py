from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import time
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(2)
driver.maximize_window()
login=driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("mohanty.mt@gmail.com")
submit=driver.find_element(By.XPATH, "//input[@id='continue']").click()
passwordtext=driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Amit@123")
passsubmit=driver.find_element(By.XPATH, "(//input[@id='signInSubmit'])[1]").click()
time.sleep(3)





