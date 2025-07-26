from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@given('I am on the radio buttons page')
def step_impl(context):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/radio-buttons")

@when('I select all color radio buttons')
def step_impl(context):
    for color in ["blue", "red", "yellow", "black"]:
        radio = context.driver.find_element(By.ID, color)
        radio.click()

@then('all selected radio buttons should be checked')
def step_impl(context):
    for color in ["blue", "red", "yellow", "black"]:
        radio = context.driver.find_element(By.ID, color)
        assert radio.is_selected()

@then('the green radio button should be visible')
def step_impl(context):
    assert context.driver.find_element(By.ID, "green").is_displayed()
    context.driver.quit()
