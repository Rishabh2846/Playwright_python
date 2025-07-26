Feature: Registration
  As a user, I want to register a new account

  Scenario: Register with valid credentials
    Given I am on the registration page
    When I enter username "admin", password "admin", and confirm password "admin"
    And I click the register button
    Then I should see the registration result
