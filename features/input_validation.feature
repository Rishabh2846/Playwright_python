Feature: Input validation
  As a user, I want to validate input fields and see correct output

  Scenario: Validate input fields
    Given I am on the input validation page
    When I fill all input fields with valid data
    And I click the display button
    Then I should see the correct output for all fields
    And I clear the output
