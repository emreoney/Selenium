from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants import *


class Test_sauceDemo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        product1 = self.driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div")

        assert product1.text == "Sauce Labs Backpack" #True dönerse giriş işlemi başarılı olmuştur.
    
    def test_loginErrorMessage(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("sdkafhsadf")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("fkasjdfhkas")

        errorMessage = self.driver.find_element(By.CLASS_NAME, "error-message-container")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_loginError(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("yanlisUsername")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("yanlisSifre")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    def test_totalProduct(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")
        numberOfProducts = len(products)
        sleep(2)
        assert numberOfProducts == 6

    def test_butonText(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        addToCardBtn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addToCardBtn.click()
        sleep(2)
        removeBtn = self.driver.find_element(By.NAME, "remove-sauce-labs-backpack")
        addToCardBtn = removeBtn
        assert addToCardBtn.text == "REMOVE"

    def test_basket(self):
        self.driver.get(BASE_DOMAIN_URL)
        sleep(2)

        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        
        addToCardBtn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addToCardBtn.click()
        sleep(2)

        cardBadge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cardBadge.text == "1"