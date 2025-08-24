from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

@given('I am on the input validation page')
def step_impl(context):
    service = EdgeService()
    options = EdgeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Edge(service=service, options=options)
    context.driver.get("https://practice.expandtesting.com/inputs")

@when('I fill all input fields with valid data')
def step_impl(context):
    from datetime import datetime
    
    # Wait for all elements to be present
    wait = WebDriverWait(context.driver, 10)
    
    # Fill number field
    number_input = wait.until(EC.presence_of_element_located((By.NAME, "input-number")))
    number_input.clear()
    number_input.send_keys("8776554321")
    
    # Fill text field
    text_input = wait.until(EC.presence_of_element_located((By.ID, "input-text")))
    text_input.clear()
    text_input.send_keys("Cypress Testing")
    
    # Fill password field
    password_input = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    password_input.clear()
    password_input.send_keys("Password123")
    
    # Fill date field with specific handling
    current_date = datetime.now().strftime("%Y-%m-%d")
    context.test_date = current_date  # Store for later assertion
    date_input = wait.until(EC.presence_of_element_located((By.NAME, "input-date")))
    
    # Clear the field first
    date_input.clear()
    
    try:
        # Try setting date with send_keys
        date_input.send_keys(current_date)
        
        # Verify the value was set
        entered_value = context.driver.execute_script("return arguments[0].value;", date_input)
        if entered_value != current_date:
            # If send_keys didn't work, try JavaScript
            context.driver.execute_script(
                f"arguments[0].value = '{current_date}'; " +
                "arguments[0].dispatchEvent(new Event('input')); " +
                "arguments[0].dispatchEvent(new Event('change'));",
                date_input
            )
    except Exception as e:
        print(f"Date input error: {e}")
        # Final fallback - try direct JavaScript value setting
        context.driver.execute_script(
            f"arguments[0].setAttribute('value', '{current_date}');",
            date_input
        )

@when('I click the display button')
def step_impl(context):
    # Wait for the button to be present
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "btn-display-inputs"))
    )
    
    # Scroll the button into view
    context.driver.execute_script("arguments[0].scrollIntoView(true);", button)
    
    # Add a small delay to let any animations complete
    context.driver.implicitly_wait(1)
    
    try:
        # Try to click normally first
        button.click()
    except:
        # If normal click fails, try JavaScript click
        context.driver.execute_script("arguments[0].click();", button)

@then('I should see the correct output for all fields')
def step_impl(context):
    # Add wait for outputs to be present
    wait = WebDriverWait(context.driver, 10)
    
    def wait_for_non_empty_text(element):
        """Wait for an element to have non-empty text"""
        return element.text.strip() != ""
    
    # Check number output
    number_output = wait.until(EC.presence_of_element_located((By.ID, "output-number")))
    wait.until(lambda _: wait_for_non_empty_text(number_output))
    assert number_output.text == "8776554321"
    
    # Check text output
    text_output = wait.until(EC.presence_of_element_located((By.ID, "output-text")))
    wait.until(lambda _: wait_for_non_empty_text(text_output))
    assert text_output.text == "Cypress Testing"
    
    # Check password output
    password_output = wait.until(EC.presence_of_element_located((By.ID, "output-password")))
    wait.until(lambda _: wait_for_non_empty_text(password_output))
    assert password_output.text == "Password123"
    
    # Check date output with improved waiting and verification
    date_output = wait.until(EC.presence_of_element_located((By.ID, "output-date")))
    
    # Wait specifically for the date output to be populated
    try:
        wait.until(lambda _: wait_for_non_empty_text(date_output))
    except:
        # If waiting fails, get the current state for debugging
        print("Debug: Button click may not have worked. Checking button state...")
        button = context.driver.find_element(By.ID, "btn-display-inputs")
        print(f"Button enabled: {button.is_enabled()}")
        print(f"Button displayed: {button.is_displayed()}")
        # Try clicking the button again
        button.click()
        # Wait again for the output
        wait.until(lambda _: wait_for_non_empty_text(date_output))
    
    actual_date = date_output.text.strip()
    expected_date = context.test_date.strip()
    
    # Print debug information
    print(f"Expected date: {expected_date}")
    print(f"Actual date: {actual_date}")
    print(f"Date input value: {context.driver.find_element(By.NAME, 'input-date').get_attribute('value')}")
    
    # Simple direct comparison first
    if actual_date == expected_date:
        return
        
    # If direct comparison fails, try to normalize both dates
    actual_digits = ''.join(c for c in actual_date if c.isdigit())
    expected_digits = ''.join(c for c in expected_date if c.isdigit())
    
    assert actual_digits == expected_digits, \
        f"Date mismatch after normalization. Expected {expected_date} (normalized: {expected_digits}), got {actual_date} (normalized: {actual_digits})"

@then('I clear the output')
def step_impl(context):
    try:
        # Find and click the clear button
        clear_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-danger.ms-2"))
        )
        clear_button.click()
        
        
    except Exception as e:
        print(f"Error during clear: {str(e)}")
    finally:
        # Always quit the driver
        context.driver.quit()
