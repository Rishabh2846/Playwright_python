from playwright.sync_api import sync_playwright
import os

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = "chromium"

def before_scenario(context, scenario):
    browser = context.playwright.chromium.launch(
        headless=os.environ.get('CI', False),
        args=['--no-sandbox', '--disable-dev-shm-usage']
    )
    context.browser = browser
    context.page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    context.page.set_default_timeout(10000)  # 10 seconds timeout

def after_scenario(context, scenario):
    if hasattr(context, 'page'):
        context.page.close()
    if hasattr(context, 'browser'):
        context.browser.close()

def after_all(context):
    context.playwright.stop()
