import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def generate_random_string(length=8):
    """Generate a random string of specified length"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-web-security')  # Disable CORS
    options.add_argument('--ignore-certificate-errors')  # Ignore SSL errors
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--no-sandbox')  # Disable sandbox for better stability
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource issues
    options.add_argument('--enable-javascript')  # Explicitly enable JavaScript
    options.page_load_strategy = 'eager'  # Load page faster by not waiting for all resources
    
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(30)  # Increase implicit wait time further
    driver.set_page_load_timeout(30)  # Set page load timeout
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 20)  # Increase explicit wait time

def wait_for_url_load(driver, url, retries=3):
    """Wait for URL to load with retries and extensive checks"""
    for attempt in range(retries):
        try:
            print(f"\nAttempting to load {url} (attempt {attempt + 1})")
            driver.get(url)
            
            # Wait for document ready state
            wait = WebDriverWait(driver, 10)
            wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            
            # Wait for jQuery if it exists
            jquery_ready = """
            try {
                if (typeof jQuery != 'undefined') {
                    return jQuery.active == 0;
                }
                return true;
            } catch(e) {
                return true;
            }
            """
            wait.until(lambda d: d.execute_script(jquery_ready))
            
            # Additional wait for any dynamic content
            time.sleep(3)
            
            # Verify we're on the right page
            current_url = driver.current_url
            print(f"Current URL: {current_url}")
            
            # Check if page has minimum expected elements
            try:
                body = driver.find_element(By.TAG_NAME, "body")
                if not body or not body.text:
                    print("Warning: Page body is empty")
            except:
                print("Warning: Could not find page body")
            
            # Try to find common form elements
            try:
                if "login" in url.lower():
                    form = driver.find_element(By.ID, "login-form")
                    print("Found login form")
                elif "register" in url.lower():
                    form = driver.find_element(By.ID, "registration-form")
                    print("Found registration form")
            except:
                print("Warning: Could not find form element")
            
            return True
        except Exception as e:
            print(f"Load attempt {attempt + 1} failed: {str(e)}")
            if attempt == retries - 1:
                driver.save_screenshot(f"load_error_{attempt}.png")
                raise
            time.sleep(3)  # Wait before retry

def click_element(driver, element):
    """Handle element click with multiple strategies and retries"""
    methods = [
        lambda: element.click(),  # Regular click
        lambda: driver.execute_script("arguments[0].click();", element),  # JS click
        lambda: element.send_keys(Keys.RETURN),  # Enter key
        lambda: driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', {bubbles: true}))", element)  # MouseEvent
    ]
    
    for method in methods:
        try:
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # Wait for scroll
            
            # Try clicking
            method()
            time.sleep(1)  # Wait after click
            return True
        except Exception as e:
            print(f"Click attempt failed: {str(e)}")
            continue
            
    raise Exception("All click attempts failed")
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)

def test_valid_login(driver, wait):
    """Test login with valid credentials"""
    # Navigate to login page with retry
    wait_for_url_load(driver, "https://practice.expandtesting.com/login")
    
    try:
        # Wait for and fill in login form
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.clear()
        username_field.send_keys("practice")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("login_error.png")
        raise
    
    # Wait for and verify success message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "You logged into a secure area!" in flash_message.text
    
    # Verify logged-in state
    logout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-logout")))
    assert logout_button.is_displayed(), "Logout button should be visible after login"

def test_invalid_login_password(driver, wait):
    """Test login with invalid password"""
    wait_for_url_load(driver, "https://practice.expandtesting.com/login")
    
    try:
        # Wait for and fill in login form
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.clear()
        username_field.send_keys("practice")
        password_field.clear()
        password_field.send_keys("WrongPassword123!")
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("invalid_password_error.png")
        raise
    
    # Verify error message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "Your password is invalid!" in flash_message.text

def test_invalid_login_username(driver, wait):
    """Test login with invalid username"""
    wait_for_url_load(driver, "https://practice.expandtesting.com/login")
    
    try:
        # Wait for and fill in login form
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        username_field.clear()
        username_field.send_keys("nonexistent_user")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("invalid_username_error.png")
        raise
    
    # Verify error message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "Your username is invalid!" in flash_message.text

def test_empty_login_fields(driver, wait):
    """Test login with empty fields"""
    wait_for_url_load(driver, "https://practice.expandtesting.com/login")
    
    try:
        # Wait for and click submit without entering credentials
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        # Make sure any existing values are cleared
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.clear()
        password_field.clear()
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("empty_fields_error.png")
        raise
    
    # Verify error message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "Username is required" in flash_message.text

def test_valid_registration(driver, wait):
    """Test successful user registration"""
    wait_for_url_load(driver, "https://practice.expandtesting.com/register")
    
    try:
        # Generate random username and password
        username = f"test_user_{generate_random_string()}"
        password = f"Pass_{generate_random_string(12)}"
        
        # Wait for and fill in registration form
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        confirm_password_field = wait.until(EC.presence_of_element_located((By.NAME, "confirmPassword")))
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn.btn-bg.btn-primary.d-block.w-100")))
        
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("registration_error.png")
        raise
    
    # Wait for and verify success message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "User created successfully" in flash_message.text

def test_registration_password_mismatch(driver, wait):
    """Test registration with mismatched passwords"""
    wait_for_url_load(driver, "https://practice.expandtesting.com/register")
    
    try:
        # Fill in registration form with different passwords
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        confirm_password_field = wait.until(EC.presence_of_element_located((By.NAME, "confirmPassword")))
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn.btn-bg.btn-primary.d-block.w-100")))
        
        username_field.clear()
        username_field.send_keys(generate_random_string())
        password_field.clear()
        password_field.send_keys("Password123!")
        confirm_password_field.clear()
        confirm_password_field.send_keys("DifferentPassword123!")
        
        # Wait before clicking
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        click_element(driver, submit_button)
        
    except Exception as e:
        driver.save_screenshot("password_mismatch_error.png")
        raise
    
    # Verify error message
    flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash_message")))
    assert "Passwords do not match" in flash_message.text
