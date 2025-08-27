import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import time

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
    driver.get("https://practice.expandtesting.com/js-dialogs")
    wait = WebDriverWait(driver, 10)
    # Wait for the page to load
    wait.until(EC.presence_of_element_located((By.ID, "js-alert")))
    # Scroll to top of page
    driver.execute_script("window.scrollTo(0, 0)")
    yield
    # Clear any remaining alerts
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        pass
    # Clear response message
    driver.refresh()
    time.sleep(0.5)

def test_alert_dialog(driver):
    """Test basic JavaScript alert dialog"""
    wait = WebDriverWait(driver, 10)
    
    # Click the alert button using JavaScript
    alert_button = wait.until(EC.presence_of_element_located((By.ID, "js-alert")))
    driver.execute_script("arguments[0].click();", alert_button)
    
    # Wait for and verify alert
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a Js Alert", "Unexpected alert text"
    
    # Accept alert
    alert.accept()
    
    # Verify response
    response = wait.until(EC.presence_of_element_located((By.ID, "dialog-response")))
    assert "OK" in response.text, "Expected 'OK' in response"

def test_confirm_dialog_accept(driver):
    """Test JavaScript confirm dialog - Accept"""
    wait = WebDriverWait(driver, 10)
    
    # Click confirm button using JavaScript
    confirm_button = wait.until(EC.presence_of_element_located((By.ID, "js-confirm")))
    driver.execute_script("arguments[0].click();", confirm_button)
    
    # Wait for and verify alert
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a Js Confirm", "Unexpected confirm dialog text"
    
    # Accept confirm dialog
    alert.accept()
    
    # Verify response
    response = wait.until(EC.presence_of_element_located((By.ID, "dialog-response")))
    assert "Ok" in response.text, "Expected 'Ok' in response for accepted confirm"

def test_confirm_dialog_dismiss(driver):
    """Test JavaScript confirm dialog - Dismiss"""
    wait = WebDriverWait(driver, 10)
    
    # Click confirm button using JavaScript
    confirm_button = wait.until(EC.presence_of_element_located((By.ID, "js-confirm")))
    driver.execute_script("arguments[0].click();", confirm_button)
    
    # Wait for and verify alert
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a Js Confirm", "Unexpected confirm dialog text"
    
    # Dismiss confirm dialog
    alert.dismiss()
    
    # Verify response
    response = wait.until(EC.presence_of_element_located((By.ID, "dialog-response")))
    assert "Cancel" in response.text, "Expected 'Cancel' in response for dismissed confirm"

def test_prompt_dialog_with_input(driver):
    """Test JavaScript prompt dialog with input"""
    wait = WebDriverWait(driver, 10)
    test_input = "Hello from Selenium!"
    
    # Set up the prompt response using JavaScript
    driver.execute_script(f'window.prompt = function() {{ return "{test_input}"; }}')
    
    # Get prompt button and click it using JavaScript
    prompt_button = wait.until(EC.presence_of_element_located((By.ID, "js-prompt")))
    driver.execute_script("arguments[0].click();", prompt_button)
    
    # Verify response contains the input
    response = wait.until(EC.presence_of_element_located((By.ID, "dialog-response")))
    assert test_input in response.text, f"Expected '{test_input}' in response"

def test_prompt_dialog_empty(driver):
    """Test JavaScript prompt dialog with empty input"""
    wait = WebDriverWait(driver, 10)
    
    # Click prompt button using JavaScript
    prompt_button = wait.until(EC.presence_of_element_located((By.ID, "js-prompt")))
    driver.execute_script("arguments[0].click();", prompt_button)
    
    # Handle the prompt dialog
    alert = wait.until(EC.alert_is_present())
    alert.send_keys("")  # Send empty string
    alert.accept()
    
    # Wait for response with text update
    response = wait.until(EC.presence_of_element_located((By.ID, "dialog-response")))
    assert response.text == "", f"Expected empty response, got: {response.text}"

def test_prompt_dialog_cancel(driver):
    """Test JavaScript prompt dialog - Cancel"""
    wait = WebDriverWait(driver, 10)
    
    # Click prompt button using JavaScript
    driver.execute_script("""
        window.promptResponse = null;
        window.onprompt = function(result) {
            window.promptResponse = result;
        };
    """)
    
    prompt_button = wait.until(EC.presence_of_element_located((By.ID, "js-prompt")))
    driver.execute_script("arguments[0].click();", prompt_button)
    
    # Handle the prompt dialog - dismiss to simulate cancel
    alert = wait.until(EC.alert_is_present())
    alert.dismiss()
    
    # Wait for a moment to let the JavaScript execute
    time.sleep(0.5)
    
    # Get the prompt response
    result = driver.execute_script("return window.promptResponse")
    assert result is None, f"Expected None when canceling prompt, got: {result}"
