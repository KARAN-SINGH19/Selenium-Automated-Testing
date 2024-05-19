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

driver.find_element(By.LINK_TEXT, "Don't have an account? Register").click()
time.sleep(2)
driver.find_element(By.ID,'floatingName').send_keys('Abdus Samad')
time.sleep(2)
driver.find_element(By.ID,'floatingEmail').send_keys('abdussamad12@gmail.com')
time.sleep(2)
driver.find_element(By.ID,'floatingAge').send_keys('21')
time.sleep(2)
driver.find_element(By.ID,'floatingPassword').send_keys('password')
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[5]/button').click()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 950)")
time.sleep(2)

selectProdBtn2=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div[3]/div/div[2]/a/button')
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(selectProdBtn2)
).click()
time.sleep(2)

addToCart2=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/div/div/button')
WebDriverWait(driver,20).until(
    EC.element_to_be_clickable(addToCart2)
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
driver.find_element(By.ID,'address').send_keys('Abu Shagara')
time.sleep(2)
driver.find_element(By.ID,'city').send_keys('SHARJAH')
time.sleep(2)
driver.find_element(By.ID,'state').send_keys('SHARJAH')
time.sleep(2)
driver.find_element(By.ID,'phone').send_keys('509814927')
time.sleep(2)
driver.find_element(By.ID,'code').send_keys('1234')
time.sleep(3)
driver.execute_script("window.scrollBy(0, 120)")
time.sleep(2)
driver.find_element(By.ID,'btn').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/div/table/tbody/tr/td[5]/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/nav/div/button').click()
time.sleep(2)
driver.quit()



