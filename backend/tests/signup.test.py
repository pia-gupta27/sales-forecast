from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_signup():
    driver.get("http://localhost:3001/signup")

    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name_input.send_keys("TestFirstName")

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("TestPassword123")

    toggle_password_visibility = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Show password')]")
    toggle_password_visibility.click()
    toggle_password_visibility.click()

    signup_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]")
    signup_button.click()

try:
    test_signup()
    print("Signup test completed successfully.")
except Exception as e:
    print(f"Signup test failed: {e}")
finally:
    driver.quit()
