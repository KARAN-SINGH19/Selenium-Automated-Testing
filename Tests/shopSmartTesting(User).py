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

driver.execute_script("window.scrollBy(0, 1000)")
time.sleep(2)

selectProdBtn=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/a/button')
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(selectProdBtn)
).click()
time.sleep(2)

addToCart=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/div/div/button')
WebDriverWait(driver,20).until(
    EC.element_to_be_clickable(addToCart)
).click()

driver.execute_script("window.scrollTo(0, 0)")
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div/div[1]/button').click()
time.sleep(2)
driver.find_element(By.TAG_NAME, 'svg').click()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/div/button[2]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 120)")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/a/button').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/div/div[2]/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]').click()


driver.find_element(By.ID,'email').send_keys('rehalkaran37@gmail.com')
time.sleep(2)
driver.find_element(By.ID,'cardNumber').send_keys('4242 4242 4242 4242')
time.sleep(2)
driver.find_element(By.ID,'cardExpiry').send_keys('02 26')
time.sleep(2)
driver.find_element(By.ID,'cardCvc').send_keys('123')
time.sleep(2)
driver.find_element(By.ID,'billingName').send_keys('Karan')
time.sleep(2)
driver.execute_script("window.scrollBy(0, 90)")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/main/div/div[2]/form/div[1]/div/div/div[3]/div/div[2]/button').click()
time.sleep(2) 
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/a/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/nav/div/button').click()
time.sleep(2)
driver.quit()