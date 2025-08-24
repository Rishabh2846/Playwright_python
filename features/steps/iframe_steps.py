from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the iframe page')
def step_impl(context):
    service = EdgeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Edge(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/iframe")

@when('I clear the text and type "{text}"')
def step_impl(context, text):
    iframe = context.driver.find_element(By.ID, "mce_0_ifr")
    context.driver.switch_to.frame(iframe)
    p = context.driver.find_element(By.TAG_NAME, "p")
    p.clear()
    p.send_keys(text)
    context.driver.switch_to.default_content()

@then('I should see "{text}" in the iframe')
def step_impl(context, text):
    iframe = context.driver.find_element(By.ID, "mce_0_ifr")
    context.driver.switch_to.frame(iframe)
    p = context.driver.find_element(By.TAG_NAME, "p")
    assert text in p.text
    context.driver.switch_to.default_content()
    context.driver.quit()
