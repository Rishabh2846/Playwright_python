Feature: Radio Buttons
  As a user, I want to select radio buttons and verify their state

  Scenario: Select all color radio buttons
    Given I am on the radio buttons page
    When I select all color radio buttons
    Then all selected radio buttons should be checked
    And the green radio button should be visible
