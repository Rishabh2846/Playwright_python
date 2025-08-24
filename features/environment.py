from selenium import webdriver
from selenium.webdriver.edge.options import Options
import platform

def before_scenario(context, scenario):
    edge_options = Options()
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--window-size=1920,1080')
    
    if platform.system().lower() == 'linux':
        # Additional options for CI environment
        edge_options.add_argument('--headless')
    
    context.driver = webdriver.Edge(options=edge_options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
