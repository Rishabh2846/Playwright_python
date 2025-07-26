Feature: JavaScript Alerts
  As a user, I want to interact with JS alert, confirm, and prompt dialogs

  Scenario: Handle alert dialog
    Given I am on the JS alerts page
    When I click the alert button
    Then I should see "OK" in the response

  Scenario: Handle confirm dialog OK
    Given I am on the JS alerts page
    When I click the confirm button and accept
    Then I should see "Ok" in the response

  Scenario: Handle confirm dialog Cancel
    Given I am on the JS alerts page
    When I click the confirm button and dismiss
    Then I should see "Cancel" in the response

  Scenario: Handle prompt dialog
    Given I am on the JS alerts page
    When I click the prompt button and enter "testing"
    Then I should see "testing" in the response
