from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@given('I am on the input validation page')
def step_impl(context):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/inputs")

@when('I fill all input fields with valid data')
def step_impl(context):
    context.driver.find_element(By.NAME, "input-number").send_keys("8776554321")
    context.driver.find_element(By.ID, "input-text").send_keys("Cypress Testing")
    context.driver.find_element(By.ID, "input-password").send_keys("Password123")
    context.driver.find_element(By.NAME, "input-date").send_keys("2023-05-05")

@when('I click the display button')
def step_impl(context):
    context.driver.find_element(By.ID, "btn-display-inputs").click()

@then('I should see the correct output for all fields')
def step_impl(context):
    assert context.driver.find_element(By.ID, "output-number").text == "8776554321"
    assert context.driver.find_element(By.ID, "output-text").text == "Cypress Testing"
    assert context.driver.find_element(By.ID, "output-password").text == "Password123"
    assert context.driver.find_element(By.ID, "output-date").text == "2023-05-05"

@then('I clear the output')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-danger.ms-2").click()
    context.driver.quit()
