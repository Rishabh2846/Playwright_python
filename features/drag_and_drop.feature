Feature: Drag and Drop
  As a user, I want to drag and drop elements on the page

  Scenario: Drag column A to column B
    Given I am on the drag and drop page
    When I drag column A to column B
    Then the columns should be swapped
