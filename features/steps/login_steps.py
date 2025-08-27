from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the login page')
def step_impl(context):
    context.page.goto("https://practice.expandtesting.com/login")
    context.page.wait_for_load_state("networkidle")

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.page.locator("#username").fill(username)
    context.page.locator("#password").fill(password)

@when('I click the login button')
def step_impl(context):
    # Wait for button to be visible and click it
    submit_button = context.page.get_by_role("button", name="Login")
    submit_button.scroll_into_view_if_needed()
    submit_button.click()
    
    # Wait for response to complete
    context.page.wait_for_load_state("networkidle")

@then('I should see login message "{message}"')
def step_impl(context, message):
    # Verify the message appears in page content
    expect(context.page.get_by_text(message)).to_be_visible()
