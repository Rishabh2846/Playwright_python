Feature: Todo App
  As a user, I want to manage my todo list

  Scenario: Check default todos
    Given I am on the todo app page
    Then I should see 2 default todos
    And the first todo should be "Pay electric bill"
    And the last todo should be "Walk the dog"

  Scenario: Add a new todo
    Given I am on the todo app page
    When I add a new todo "Feed the cat"
    Then the new todo should be added to the list
    When I mark the new todo as completed
    Then the new todo should be marked as completed
