from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the registration page')
def step_impl(context):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/login")
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/register']").click()

@when('I enter username "{username}", password "{password}", and confirm password "{confirm_password}"')
def step_impl(context, username, password, confirm_password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "confirmPassword").send_keys(confirm_password)

@when('I click the register button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-bg.btn-primary.d-block.w-100").click()

@then('I should see the registration result')
def step_impl(context):
    # Add assertion for registration result if the page shows a message
    context.driver.quit()
