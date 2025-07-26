from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Uncomment for headless mode
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/login")

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the login button')
def step_impl(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    import time
    context.driver.execute_script("arguments[0].scrollIntoView(true);", button)
    WebDriverWait(context.driver, 2).until(EC.visibility_of(button))
    time.sleep(1)
    try:
        button.click()
    except Exception:
        context.driver.execute_script("arguments[0].click();", button)

@then('I should see "{expected}"')
def step_impl(context, expected):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert expected in context.driver.page_source
    context.driver.quit()
