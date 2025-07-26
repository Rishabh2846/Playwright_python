import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="module")
def driver():
    service = ChromeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_alert_dialog(driver):
    driver.get("https://practice.expandtesting.com/js-dialogs")
    driver.find_element(By.ID, "js-alert").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a Js Alert"
    alert.accept()
    assert "OK" in driver.find_element(By.ID, "dialog-response").text

def test_confirm_ok(driver):
    driver.get("https://practice.expandtesting.com/js-dialogs")
    driver.find_element(By.ID, "js-confirm").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a Js Confirm"
    alert.accept()
    assert "Ok" in driver.find_element(By.ID, "dialog-response").text

def test_confirm_cancel(driver):
    driver.get("https://practice.expandtesting.com/js-dialogs")
    driver.find_element(By.ID, "js-confirm").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a Js Confirm"
    alert.dismiss()
    assert "Cancel" in driver.find_element(By.ID, "dialog-response").text

def test_prompt_dialog(driver):
    driver.get("https://practice.expandtesting.com/js-dialogs")
    driver.execute_script("window.prompt = function(){return 'testing';}")
    driver.find_element(By.ID, "js-prompt").click()
    assert "testing" in driver.find_element(By.ID, "dialog-response").text
