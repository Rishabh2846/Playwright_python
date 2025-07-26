Feature: Login functionality
  As a user, I want to login to the application with valid and invalid credentials

  Scenario Outline: Login with different credentials
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see "<expected>"

    Examples:
      | username  | password              | expected                              |
      | practice  | SuperSecretPassword!  | You logged into a secure area!        |
      | admin     | admin                 | Your password is invalid!             |
