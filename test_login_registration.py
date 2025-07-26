import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Update the path to your chromedriver if needed
    service = ChromeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Remove if you want to see the browser
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, "username").send_keys("practice")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "You logged into a secure area!" in driver.page_source

def test_invalid_password(driver):
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "Your password is invalid!" in driver.page_source

def test_valid_registration(driver):
    driver.get("https://practice.expandtesting.com/login")
    driver.find_element(By.CSS_SELECTOR, "a[href='/register']").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "confirmPassword").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-bg.btn-primary.d-block.w-100").click()
    # Add an assertion here if the registration page gives a success message
