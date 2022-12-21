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
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        product1 = self.driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div")

        assert product1.text == "Sauce Labs Backpack" #True dönerse giriş işlemi başarılı olmuştur.
    
    def test_loginErrorMessage(self):
        self.driver.get(BASE_DOMAIN_URL)
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("sdkafhsadf")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("fkasjdfhkas")

        errorMessage = self.driver.find_element(By.CLASS_NAME, "error-message-container")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_loginError(self):
        self.driver.get(BASE_DOMAIN_URL)
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("yanlisUsername")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("yanlisSifre")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        errorMessage = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    def test_totalProduct(self):
        self.driver.get(BASE_DOMAIN_URL)
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")
        numberOfProducts = len(products)
        
        assert numberOfProducts == 6

    def test_butonText(self):
        self.driver.get(BASE_DOMAIN_URL)
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        
        addToCardBtnID = ADD_TO_CARD_BTN_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,addToCardBtnID)))
        addToCardBtn = self.driver.find_element(By.ID,addToCardBtnID)
        addToCardBtn.click()

        removeBtnName = "remove-sauce-labs-backpack"
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,removeBtnName)))
        removeBtn = self.driver.find_element(By.NAME, "remove-sauce-labs-backpack")
        addToCardBtn = removeBtn
        assert addToCardBtn.text == "REMOVE"

    def test_basket(self):
        self.driver.get(BASE_DOMAIN_URL)
        usernameID = USERNAME_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,usernameID)))
        username = self.driver.find_element(By.ID, usernameID)
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        addToCardBtnID = ADD_TO_CARD_BTN_ID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,addToCardBtnID)))
        addToCardBtn = self.driver.find_element(By.ID,addToCardBtnID)
        addToCardBtn.click()
        
        
        cardBadge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cardBadge.text == "1"