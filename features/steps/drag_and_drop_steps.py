from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

@given('I am on the drag and drop page')
def step_impl(context):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/drag-and-drop")

@when('I drag column A to column B')
def step_impl(context):
    source = context.driver.find_element(By.ID, "column-a")
    target = context.driver.find_element(By.ID, "column-b")
    ActionChains(context.driver).drag_and_drop(source, target).perform()

@then('the columns should be swapped')
def step_impl(context):
    # Optionally, add an assertion if the UI changes after drag and drop
    context.driver.quit()
