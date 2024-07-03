from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_sales_prediction_form():
    driver.get("http://localhost:3000")  

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Item_Weight"))).send_keys("20")
    driver.find_element(By.NAME, "Item_Fat_Content").send_keys("Low Fat")
    driver.find_element(By.NAME, "Item_Visibility").send_keys("0.1")
    driver.find_element(By.NAME, "Item_MRP").send_keys("150")
    driver.find_element(By.NAME, "Outlet_Size").send_keys("Medium")
    driver.find_element(By.NAME, "Outlet_Location_Type").send_keys("Tier 1")
    driver.find_element(By.NAME, "OutletType").send_keys("Supermarket Type 1")
    driver.find_element(By.NAME, "Outlet_Age").send_keys("10")
    driver.find_element(By.NAME, "ItemType").send_keys("Breads")
    driver.find_element(By.NAME, "outlet_identifier").send_keys("OUT013")
    
    driver.find_element(By.ID, "button").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "predictionResult")))

test_sales_prediction_form()
driver.quit()
