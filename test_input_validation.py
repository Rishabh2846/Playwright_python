import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime, timedelta

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = webdriver.ChromeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup(driver):
    # Navigate to the page before each test
    driver.get("https://practice.expandtesting.com/inputs")
    wait = WebDriverWait(driver, 10)
    # Wait for the page to load
    wait.until(EC.presence_of_element_located((By.ID, "btn-display-inputs")))
    
    # Clear any existing data
    clear_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.btn.btn-outline-danger.ms-2")))
    driver.execute_script("arguments[0].click();", clear_btn)
    time.sleep(0.5)  # Wait for clear to complete
    yield
    
    # Scroll to top after each test
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(0.5)

def test_valid_inputs(driver):
    """Test all input fields with valid data"""
    wait = WebDriverWait(driver, 10)
    
    # Test data
    test_date = datetime.now().strftime("%Y-%m-%d")
    test_data = {
        "number": "8776554321",
        "text": "Selenium Testing",
        "password": "SecurePass123!",
        "date": test_date
    }
    
    # Fill in the inputs
    number_input = wait.until(EC.presence_of_element_located((By.NAME, "input-number")))
    number_input.send_keys(test_data["number"])
    
    text_input = wait.until(EC.presence_of_element_located((By.ID, "input-text")))
    text_input.send_keys(test_data["text"])
    
    password_input = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    password_input.send_keys(test_data["password"])
    
    # For date input, use JavaScript to set the value
    date_input = wait.until(EC.presence_of_element_located((By.NAME, "input-date")))
    driver.execute_script(f"arguments[0].value = '{test_date}'", date_input)
    
    # Scroll the display button into view and click it
    display_btn = wait.until(EC.element_to_be_clickable((By.ID, "btn-display-inputs")))
    driver.execute_script("arguments[0].scrollIntoView(true);", display_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", display_btn)
    
    # Verify outputs
    assert wait.until(EC.presence_of_element_located((By.ID, "output-number"))).text == test_data["number"]
    assert wait.until(EC.presence_of_element_located((By.ID, "output-text"))).text == test_data["text"]
    assert wait.until(EC.presence_of_element_located((By.ID, "output-password"))).text == test_data["password"]
    
    # Verify date output
    date_output = wait.until(EC.presence_of_element_located((By.ID, "output-date")))
    displayed_date = date_output.text
    assert displayed_date == test_date, f"Expected date {test_date}, got {displayed_date}"

def test_number_input_validation(driver):
    """Test number input field validation"""
    wait = WebDriverWait(driver, 10)
    
    number_input = wait.until(EC.presence_of_element_located((By.NAME, "input-number")))
    display_btn = wait.until(EC.presence_of_element_located((By.ID, "btn-display-inputs")))
    
    # Test invalid input (letters)
    number_input.send_keys("abc123")
    input_value = number_input.get_attribute("value")
    assert input_value == "123", f"Only numbers should be accepted, got: {input_value}"
    
    # Test decimal numbers
    number_input.clear()
    number_input.send_keys("123")
    input_value = number_input.get_attribute("value")
    assert input_value == "123", f"Expected 123, got {input_value}"
    
    # Click display and verify
    driver.execute_script("arguments[0].scrollIntoView(true);", display_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", display_btn)
    
    output = wait.until(EC.presence_of_element_located((By.ID, "output-number")))
    assert output.text == "123", f"Expected 123 in output, got {output.text}"

def test_date_input_validation(driver):
    """Test date input field validation"""
    wait = WebDriverWait(driver, 10)
    
    date_input = wait.until(EC.presence_of_element_located((By.NAME, "input-date")))
    display_btn = wait.until(EC.presence_of_element_located((By.ID, "btn-display-inputs")))
    
    # Test current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    driver.execute_script(f"arguments[0].value = '{current_date}'", date_input)
    
    # Click display and verify
    driver.execute_script("arguments[0].scrollIntoView(true);", display_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", display_btn)
    
    date_output = wait.until(EC.presence_of_element_located((By.ID, "output-date")))
    assert date_output.text == current_date, f"Expected {current_date}, got {date_output.text}"

def test_password_strength(driver):
    """Test password input field with various patterns"""
    wait = WebDriverWait(driver, 10)
    
    password_input = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    display_btn = wait.until(EC.presence_of_element_located((By.ID, "btn-display-inputs")))
    
    test_passwords = [
        "short",  # Short password
        "longerpassword",  # No special chars
        "Password123!",  # Strong password
        "!@#$%^&*()",  # Special chars
    ]
    
    for password in test_passwords:
        # Clear the input and enter new password
        password_input.clear()
        password_input.send_keys(password)
        
        # Click display using JavaScript
        driver.execute_script("arguments[0].scrollIntoView(true);", display_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", display_btn)
        
        # Verify the password was displayed correctly
        output = wait.until(EC.presence_of_element_located((By.ID, "output-password")))
        assert output.text == password, f"Expected password '{password}', got '{output.text}'"
