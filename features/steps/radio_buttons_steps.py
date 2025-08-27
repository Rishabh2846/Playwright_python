from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the radio buttons page')
def step_impl(context):
    context.page.goto("https://practice.expandtesting.com/radio-buttons")
    context.page.wait_for_load_state("networkidle")

@when('I select all color radio buttons')
def step_impl(context):
    for color in ["blue", "red", "yellow", "black"]:
        radio = context.page.get_by_id(color)
        radio.click()
        # Wait for a brief moment to ensure the click registers
        context.page.wait_for_timeout(100)

@then('all selected radio buttons should be checked')
def step_impl(context):
    for color in ["blue", "red", "yellow", "black"]:
        radio = context.page.get_by_id(color)
        expect(radio).to_be_checked()

@then('the green radio button should be visible')
def step_impl(context):
    green_radio = context.page.get_by_id("green")
    expect(green_radio).to_be_visible()
