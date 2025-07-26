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

def test_hover_users(driver):
    driver.get("https://practice.expandtesting.com/hovers")
    for i in range(1, 4):
        img = driver.find_element(By.CSS_SELECTOR, f"img[data-testid='img-user-{i}']")
        ActionChains(driver).move_to_element(img).perform()
        h5 = driver.find_element(By.TAG_NAME, "h5")
        assert f"name: user{i}" in h5.text

def test_hover_and_click_user_links(driver):
    driver.get("https://practice.expandtesting.com/hovers")
    for i in range(1, 4):
        img = driver.find_element(By.CSS_SELECTOR, f"img[data-testid='img-user-{i}']")
        ActionChains(driver).move_to_element(img).perform()
        link = driver.find_element(By.CSS_SELECTOR, f"a[href='/users/{i}']")
        link.click()
        assert f"/users/{i}" in driver.current_url
        h2 = driver.find_element(By.TAG_NAME, "h2")
        assert f"Welcome user{i}" in h2.text
        driver.back()
