from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.get("http://localhost:3001/signin") 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("your_email@example.com")  
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("your_password")  
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
)
sign_in_button.click()
driver.quit()
