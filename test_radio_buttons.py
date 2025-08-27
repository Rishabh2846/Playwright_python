import pytest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = EdgeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-web-security')  # Disable CORS
    options.add_argument('--ignore-certificate-errors')  # Ignore SSL errors
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--no-sandbox')  # Disable sandbox for better stability
    options.page_load_strategy = 'normal'  # Use normal page load strategy
    
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)  # Set implicit wait
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)  # Set explicit wait timeout

def test_radio_buttons(driver, wait):
    """Test radio button functionality"""
    # Navigate to the radio buttons test page
    driver.get("https://practice.expandtesting.com/radio-buttons/")
    
    try:
        # Get all radio buttons by name group
        color_radios = driver.find_elements(By.CSS_SELECTOR, 'input[name="color"]')
        sport_radios = driver.find_elements(By.CSS_SELECTOR, 'input[name="sport"]')
        
        # Helper function to test a group of radio buttons
        def test_radio_group(radios, group_name):
            print(f"\nTesting {group_name} radio buttons:")
            for radio in radios:
                if radio.is_enabled():
                    # Scroll the radio button into view
                    driver.execute_script("arguments[0].scrollIntoView(true);", radio)
                    # Add a small wait to ensure the page has settled after scrolling
                    time.sleep(0.5)
                    # Click the radio button
                    radio.click()
                    
                    # Verify this radio button is selected
                    assert radio.is_selected(), f"Radio button {radio.get_attribute('id')} should be selected"
                    
                    # Verify other radio buttons are not selected
                    for other in radios:
                        if other != radio and other.is_enabled():
                            assert not other.is_selected(), f"Radio button {other.get_attribute('id')} should not be selected"
        
        # Test color radio buttons
        test_radio_group(color_radios, "color")
        
        # Test sport radio buttons
        test_radio_group(sport_radios, "sport")
            
    except TimeoutException as e:
        print(f"Timeout while waiting for radio button: {str(e)}")
        raise
    except Exception as e:
        print(f"Error during radio button test: {str(e)}")
        raise

def test_disabled_radio_button(driver, wait):
    """Test disabled radio button behavior"""
    try:
        # Get all radio buttons
        radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
        
        # Find disabled buttons
        disabled_buttons = [radio for radio in radio_buttons if not radio.is_enabled()]
        
        if not disabled_buttons:
            pytest.skip("No disabled radio buttons found on the page")
            
        print("\nTesting disabled radio buttons:")
        for disabled_radio in disabled_buttons:
            # Print information about the disabled button
            print(f"Found disabled radio: {disabled_radio.get_attribute('id')}")
            
            # Verify it exists and is disabled
            assert disabled_radio.is_displayed(), "Disabled radio button should be visible"
            assert not disabled_radio.is_enabled(), "Radio button should be disabled"
            
            # Verify it cannot be selected
            try:
                disabled_radio.click()  # This should not work
            except:
                pass  # Expected to fail
            
            # Verify it's still not selected
            assert not disabled_radio.is_selected(), "Disabled radio button should not be selectable"
        
    except Exception as e:
        print(f"Error testing disabled radio button: {str(e)}")
        raise
