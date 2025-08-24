from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import platform
import os

def before_scenario(context, scenario):
    is_ci = os.environ.get('CI', False)
    
    if is_ci:
        # Use Chromium in CI environment
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--headless=new')
        options.add_argument('--window-size=1920,1080')
        context.driver = webdriver.Chrome(options=options)
    else:
        # Use Edge for local development
        options = EdgeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        context.driver = webdriver.Edge(options=options)
    
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
