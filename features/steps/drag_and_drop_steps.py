from behave import given, when, then
import time

@given('I am on the drag and drop page')
def step_impl(context):
    context.page.goto("https://practice.expandtesting.com/drag-and-drop")
    # Wait for the page to be fully loaded
    context.page.wait_for_load_state("networkidle")

@when('I drag column A to column B')
def step_impl(context):
    # Get the source and target elements
    source = context.page.locator("#column-a")
    target = context.page.locator("#column-b")
    
    # Store initial texts for verification
    context.initial_source_text = source.inner_text()
    context.initial_target_text = target.inner_text()
    
    try:
        # First try: Use Playwright's native drag and drop
        source.drag_to(target)
        time.sleep(0.5)
    except Exception as e:
        print(f"Native drag and drop failed: {str(e)}")
        # Fallback to mouse events
        source_box = source.bounding_box()
        target_box = target.bounding_box()
        
        context.page.mouse.move(
            source_box["x"] + source_box["width"] / 2,
            source_box["y"] + source_box["height"] / 2
        )
        context.page.mouse.down()
        context.page.mouse.move(
            target_box["x"] + target_box["width"] / 2,
            target_box["y"] + target_box["height"] / 2
        )
        context.page.mouse.up()
        time.sleep(0.5)

@then('the columns should be swapped')
def step_impl(context):
    # Get the elements again after drag and drop
    source = context.page.locator("#column-a")
    target = context.page.locator("#column-b")
    
    # Wait for potential animations to complete
    context.page.wait_for_timeout(1000)
    
    # Get the current text of both elements
    source_text = source.inner_text()
    target_text = target.inner_text()
    
    # Verify that the texts have been swapped
    assert source_text == context.initial_target_text, \
        f"Expected source text to be {context.initial_target_text}, but got {source_text}"
    assert target_text == context.initial_source_text, \
        f"Expected target text to be {context.initial_source_text}, but got {target_text}"
