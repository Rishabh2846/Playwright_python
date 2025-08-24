from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@given('I am on the todo app page')
def step_impl(context):
    service = EdgeService()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Edge(service=service, options=options)
    context.driver.get("https://example.cypress.io/todo")

@then('I should see 2 default todos')
def step_impl(context):
    todos = context.driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert len(todos) == 2

@then('the first todo should be "Pay electric bill"')
def step_impl(context):
    todos = context.driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert todos[0].text == "Pay electric bill"

@then('the last todo should be "Walk the dog"')
def step_impl(context):
    todos = context.driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert todos[-1].text == "Walk the dog"

@when('I add a new todo "{new_item}"')
def step_impl(context, new_item):
    input_box = context.driver.find_element(By.CSS_SELECTOR, "[data-test=new-todo]")
    input_box.send_keys(new_item + "\n")

@then('the new todo should be added to the list')
def step_impl(context):
    todos = context.driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert todos[-1].text == "Feed the cat"

@when('I mark the new todo as completed')
def step_impl(context):
    checkbox = context.driver.find_element(By.CSS_SELECTOR, ".todo-list li:last-child .toggle")
    checkbox.click()

@then('the new todo should be marked as completed')
def step_impl(context):
    completed = context.driver.find_element(By.CSS_SELECTOR, ".todo-list li.completed")
    assert completed.text == "Feed the cat"
    context.driver.quit()
