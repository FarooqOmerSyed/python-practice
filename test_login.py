import selenium
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'

def test_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(11)
    driver.maximize_window()
    driver.get(url)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(6)
    driver.find_element(By.ID, 'login-button').click()
    assert 'Swag Labs' in driver.title
    driver.quit()
 
 
