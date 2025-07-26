import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="module")
def driver():
    service = ChromeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    driver.get("https://practice.expandtesting.com/drag-and-drop")
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    ActionChains(driver).drag_and_drop(source, target).perform()
    # Optionally, add assertion to check if drag and drop was successful
