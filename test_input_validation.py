import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_input_validation(driver):
    driver.get("https://practice.expandtesting.com/inputs")
    driver.find_element(By.NAME, "input-number").send_keys("8776554321")
    driver.find_element(By.ID, "input-text").send_keys("Cypress Testing")
    driver.find_element(By.ID, "input-password").send_keys("Password123")
    driver.find_element(By.NAME, "input-date").send_keys("2023-05-05")
    driver.find_element(By.ID, "btn-display-inputs").click()
    assert driver.find_element(By.ID, "output-number").text == "8776554321"
    assert driver.find_element(By.ID, "output-text").text == "Cypress Testing"
    assert driver.find_element(By.ID, "output-password").text == "Password123"
    assert driver.find_element(By.ID, "output-date").text == "2023-05-05"
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-danger.ms-2").click()
