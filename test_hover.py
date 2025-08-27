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
    # Set a reasonable window size
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

def test_hover_users(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/hovers")
    
    for i in range(1, 4):
        # Wait for and find the figure element
        figure_locator = (By.CSS_SELECTOR, f"div.figure:nth-of-type({i})")
        figure = wait.until(EC.presence_of_element_located(figure_locator))
        
        # Find the image within the figure
        img = figure.find_element(By.TAG_NAME, "img")
        
        # Scroll the image into view
        driver.execute_script("arguments[0].scrollIntoView(true);", img)
        time.sleep(0.5)  # Wait for scroll to complete
        
        # Perform hover action
        ActionChains(driver).move_to_element(img).perform()
        time.sleep(0.5)  # Wait for hover effect
        
        # Find and verify the user name
        h5 = figure.find_element(By.TAG_NAME, "h5")
        assert f"name: user{i}" in h5.text.lower(), f"Expected 'name: user{i}' in '{h5.text}'"

def test_hover_and_click_user_links(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practice.expandtesting.com/hovers")
    
    for i in range(1, 4):
        # Wait for and find the figure element
        figure_locator = (By.CSS_SELECTOR, f"div.figure:nth-of-type({i})")
        figure = wait.until(EC.presence_of_element_located(figure_locator))
        
        # Find the image within the figure
        img = figure.find_element(By.TAG_NAME, "img")
        
        # Scroll the image into view
        driver.execute_script("arguments[0].scrollIntoView(true);", img)
        time.sleep(0.5)  # Wait for scroll to complete
        
        # Perform hover action
        ActionChains(driver).move_to_element(img).perform()
        time.sleep(0.5)  # Wait for hover effect
        
        # Find and click the link within the figure
        link = figure.find_element(By.TAG_NAME, "a")
        driver.execute_script("arguments[0].click();", link)
        
        # Wait for navigation to complete and verify the URL
        wait.until(lambda d: f"/users/{i}" in d.current_url)
        
        # Wait for and verify the user page heading
        heading_locator = (By.TAG_NAME, "h1")
        heading = wait.until(EC.visibility_of_element_located(heading_locator))
        assert "User Profile page" in heading.text, "Expected user profile page heading"
        
        # Go back to the hover page
        driver.back()
        
        # Wait for the hover page to load again
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "figure")))
