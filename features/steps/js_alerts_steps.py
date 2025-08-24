from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@given('I am on the JS alerts page')
def step_impl(context):
    service = EdgeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Edge(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/js-dialogs")

@when('I click the alert button')
def step_impl(context):
    context.driver.find_element(By.ID, "js-alert").click()
    alert = context.driver.switch_to.alert
    assert alert.text == "I am a Js Alert"
    alert.accept()

@then('I should see alert OK in the response')
def step_impl(context):
    assert "OK" in context.driver.find_element(By.ID, "dialog-response").text

@when('I click the confirm button and accept')
def step_impl(context):
    context.driver.find_element(By.ID, "js-confirm").click()
    alert = context.driver.switch_to.alert
    assert alert.text == "I am a Js Confirm"
    alert.accept()

@then('I should see confirm OK in the response')
def step_impl(context):
    assert "Ok" in context.driver.find_element(By.ID, "dialog-response").text

@when('I click the confirm button and dismiss')
def step_impl(context):
    context.driver.find_element(By.ID, "js-confirm").click()
    alert = context.driver.switch_to.alert
    assert alert.text == "I am a Js Confirm"
    alert.dismiss()

@then('I should see "Cancel" in the response')
def step_impl(context):
    assert "Cancel" in context.driver.find_element(By.ID, "dialog-response").text

@when('I click the prompt button and enter "{text}"')
def step_impl(context, text):
    context.driver.execute_script(f"window.prompt = function(){{return '{text}';}}")
    context.driver.find_element(By.ID, "js-prompt").click()

@then('I should see "{text}" in the response')
def step_impl(context, text):
    assert text in context.driver.find_element(By.ID, "dialog-response").text
    context.driver.quit()
