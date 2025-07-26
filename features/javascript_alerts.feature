Feature: JavaScript Alerts Testing
    As a user
    I want to interact with JavaScript alerts
    So that I can test alert functionality

    Scenario: Handle simple alert
        Given I am on the JS alerts page
        When I click the alert button
        Then I should see alert OK in the response

    Scenario: Handle confirm alert - Accept
        Given I am on the JS alerts page
        When I click the confirm button and accept
        Then I should see confirm OK in the response

    Scenario: Handle confirm alert - Dismiss
        Given I am on the JS alerts page
        When I click the confirm button and dismiss
        Then I should see "Cancel" in the response

    Scenario: Handle prompt with text input
        Given I am on the JS alerts page
        When I click the prompt button and enter "Test Message"
        Then I should see "Test Message" in the response
