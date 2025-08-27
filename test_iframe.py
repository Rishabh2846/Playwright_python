import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = webdriver.ChromeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

def test_iframe_content(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/iframe")
    
    # Wait for iframe to be present
    iframe = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
    
    # Switch to iframe
    driver.switch_to.frame(iframe)
    
    # Check initial content
    p = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    initial_text = p.text
    assert "Your content goes here" in initial_text, "Expected default content not found"
    
    # Switch back to main content
    driver.switch_to.default_content()

def test_iframe_edit(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/iframe")
    
    # Wait for iframe to be present
    iframe = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
    
    # Switch to iframe
    driver.switch_to.frame(iframe)
    
    # Edit content
    p = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    p.clear()
    test_text = "This is a test message from Selenium!"
    p.send_keys(test_text)
    
    # Wait for text to be present and get updated content
    time.sleep(1)  # Add a small delay for the editor to update
    p = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    assert test_text == p.get_attribute("textContent"), f"Expected '{test_text}' but got '{p.get_attribute('textContent')}'"
    
    # Switch back to main content to complete the test
    driver.switch_to.default_content()