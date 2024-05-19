from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.implicitly_wait(20)
driver.get('http://localhost:3000/')
driver.maximize_window()

loginBtn = driver.find_element(By.LINK_TEXT, 'Login')
time.sleep(3)
loginBtn.click()
time.sleep(2)

emailField=driver.find_element(By.ID,'floatingEmail').send_keys('admin12@gmail.com')
time.sleep(3)
passwordField=driver.find_element(By.ID,'floatingPassword').send_keys('password')
time.sleep(3)
submitBtn=driver.find_element(By.TAG_NAME,'button').click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,'Users').click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,'User Feedback').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/nav/div/button').click()
time.sleep(3)
driver.quit()


