from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the hover page')
def step_impl(context):
    context.page.goto("https://practice.expandtesting.com/hovers")
    # Wait for all user avatars to be visible
    context.page.wait_for_selector(".figure", state="visible")

@when('I hover over user {number}$')
def step_impl(context, number):
    # Hover over the specified user
    user = context.page.locator(f".figure:nth-child({number})")
    user.hover()
    context.page.wait_for_timeout(500)  # Small wait for hover effect

@then('I should see user info "{text}"')
def step_impl(context, text):
    # After hovering, the user info should be visible
    info = context.page.get_by_text(text)
    expect(info).to_be_visible()

@when('I hover over user {number} and click the link')
def step_impl(context, number):
    # Hover and click the link for the specified user
    user = context.page.locator(f".figure:nth-child({number})")
    user.hover()
    context.page.wait_for_timeout(500)  # Wait for hover effect
    
    # Click the profile link
    link = user.locator("a")
    link.click()
    
    # Wait for navigation or response
    context.page.wait_for_load_state("networkidle")
