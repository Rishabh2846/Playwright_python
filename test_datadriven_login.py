import pytest
import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load test data from JSON file
def load_testdata():
    with open('testdata1.json', 'r') as f:
        return json.load(f)

testdata = load_testdata()

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("userdata", testdata.values())
def test_login_datadriven(driver, userdata):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/login")
    
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    username_field.send_keys(userdata['username'])
    
    password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys(userdata['password'])
    
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)  # Wait for the response
    assert userdata['expected_message'] in driver.page_source
