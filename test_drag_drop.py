import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    service = EdgeService()
    options = webdriver.ChromeOptions()
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/drag-and-drop")
    
    # Wait for elements to be present
    source = wait.until(EC.presence_of_element_located((By.ID, "column-a")))
    target = wait.until(EC.presence_of_element_located((By.ID, "column-b")))
    
    # Get initial text values
    initial_source_text = source.text
    initial_target_text = target.text
    
    # Ensure viewport is large enough
    driver.set_window_size(1024, 768)
    
    # Use the Selenium API directly
    actions = ActionChains(driver)
    
    # Move mouse to the source element
    actions.move_to_element(source)
    actions.pause(0.5)
    
    # Click and hold
    actions.click_and_hold()
    actions.pause(0.5)
    
    # Move to target
    actions.move_to_element(target)
    actions.pause(0.5)
    
    # Release
    actions.release()
    
    # Perform all actions
    actions.perform()
    
    # Wait for animation
    time.sleep(1)
    
    # If the first attempt didn't work, try JavaScript approach
    if source.text == initial_source_text:
        js_code = """
        var src = arguments[0];
        var tgt = arguments[1];
        src.setAttribute('draggable', true);
        var dataTransfer = {
            dropEffect: '',
            effectAllowed: 'all',
            files: [],
            items: {},
            types: [],
            setData: function (format, data) {
                this.items[format] = data;
                this.types.push(format);
            },
            getData: function (format) {
                return this.items[format];
            },
            clearData: function (format) { }
        };
        var dragEvent = document.createEvent('DragEvent');
        dragEvent.initMouseEvent('dragstart', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        dragEvent.dataTransfer = dataTransfer;
        src.dispatchEvent(dragEvent);
        var dropEvent = document.createEvent('DragEvent');
        dropEvent.initMouseEvent('drop', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        dropEvent.dataTransfer = dataTransfer;
        tgt.dispatchEvent(dropEvent);
        var dragEndEvent = document.createEvent('DragEvent');
        dragEndEvent.initMouseEvent('dragend', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        src.dispatchEvent(dragEndEvent);
        """
        driver.execute_script(js_code, source, target)
        time.sleep(1)
    
    # Wait for the elements to update
    time.sleep(1)
    
    # Get final text values
    final_source_text = source.text
    final_target_text = target.text
    
    # Verify the text values have swapped
    assert final_source_text == initial_target_text, f"Source element should have target's text. Expected: {initial_target_text}, Got: {final_source_text}"
    assert final_target_text == initial_source_text, f"Target element should have source's text. Expected: {initial_source_text}, Got: {final_target_text}"
