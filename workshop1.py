from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://tr-tr.facebook.com/")
driver.maximize_window()
sleep(2)


email = driver.find_element(By.NAME, "email")
email.click()
email.send_keys("denemeemail")
sleep(2)

password = driver.find_element(By.NAME, "pass")
password.click()
password.send_keys("denemesifre")
sleep(2)

emailText = email.get_attribute('value')
passwordText= password.get_attribute('value')


loginBtn = driver.find_element(By.NAME, "login")
loginBtn.click()
sleep(5)


if(emailText == "denemeemail" and passwordText == "denemesifre"):
        print("Test Başarılı")
else:
        print("Test başarısız")

