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

def test_radio_buttons(driver):
    driver.get("https://practice.expandtesting.com/radio-buttons")
    for color in ["blue", "red", "yellow", "black"]:
        radio = driver.find_element(By.ID, color)
        radio.click()
        assert radio.is_selected()
    assert driver.find_element(By.ID, "green").is_displayed()
