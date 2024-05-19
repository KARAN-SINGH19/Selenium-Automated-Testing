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

emailField=driver.find_element(By.ID,'floatingEmail').send_keys('rehalkaran37@gmail.com')
time.sleep(3)
passwordField=driver.find_element(By.ID,'floatingPassword').send_keys('password')
time.sleep(3)
submitBtn=driver.find_element(By.TAG_NAME,'button').click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,'Profile').click()
time.sleep(2)
driver.find_element(By.ID,'name').send_keys('Karan Singh')
time.sleep(2)
driver.find_element(By.ID,'age').send_keys('21')
time.sleep(2)
driver.find_element(By.ID,'btn1').click()
time.sleep(3)

driver.find_element(By.ID,'address').send_keys('Al,Julan')
time.sleep(2)
driver.find_element(By.ID,'btn2').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/nav/div/button').click()
time.sleep(2)
driver.quit()