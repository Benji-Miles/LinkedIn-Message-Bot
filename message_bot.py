from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

driver = webdriver.Chrome("Path_to_chrome_driver")
driver.get("https://www.linkedin.com")

username = driver.find_element(by=By.NAME, value="session_key")
password = driver.find_element(by=By.NAME, value="session_password")

username.send_keys('YOUR_EMAIL')
password.send_keys('YOUR_PASSWORD')
time.sleep(5)

submit = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
submit.click()
time.sleep(10)