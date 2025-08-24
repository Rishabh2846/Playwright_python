import pytest
import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Load test data from JSON file
def load_testdata():
    with open(r'C:\Users\Rishabh Sinha\Documents\Selenium_python\testdata1.json', 'r') as f:
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

@pytest.mark.parametrize("userdata", testdata)
def test_login_datadriven(driver, userdata):
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, "username").send_keys(userdata['name'])
    driver.find_element(By.ID, "password").send_keys(userdata['password'])
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert userdata['expected'] in driver.page_source
