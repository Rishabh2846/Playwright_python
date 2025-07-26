Feature: Iframe editing
  As a user, I want to edit text inside an iframe

  Scenario: Edit text in iframe
    Given I am on the iframe page
    When I clear the text and type "This is my new text"
    Then I should see "This is my new text" in the iframe
