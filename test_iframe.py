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

def test_iframe_edit(driver):
    driver.get("https://practice.expandtesting.com/iframe")
    iframe = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(iframe)
    p = driver.find_element(By.TAG_NAME, "p")
    p.clear()
    p.send_keys("This is my new text")
    assert "This is my new text" in p.text
    driver.switch_to.default_content()
