import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="module")
def driver():
    service = ChromeService()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_todo_app(driver):
    driver.get("https://example.cypress.io/todo")
    # Check default todos
    todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert len(todos) == 2
    assert todos[0].text == "Pay electric bill"
    assert todos[1].text == "Walk the dog"
    # Add a new todo
    new_item = "Feed the cat"
    input_box = driver.find_element(By.CSS_SELECTOR, "[data-test=new-todo]")
    input_box.send_keys(new_item + "\n")
    todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert todos[-1].text == new_item
    # Mark as completed
    checkbox = driver.find_element(By.CSS_SELECTOR, ".todo-list li:last-child .toggle")
    checkbox.click()
    completed = driver.find_element(By.CSS_SELECTOR, ".todo-list li.completed")
    assert completed.text == new_item
