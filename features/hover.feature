Feature: Hover functionality
  As a user, I want to see user info and click links after hovering

  Scenario: Hover over each user and check info
    Given I am on the hover page
    When I hover over user 1
    Then I should see user info "name: user1"
    When I hover over user 2
    Then I should see user info "name: user2"
    When I hover over user 3
    Then I should see user info "name: user3"

  Scenario: Click user links after hover
    Given I am on the hover page
    When I hover over user 1 and click the link
    Then I should see user info "Welcome user1"
    When I hover over user 2 and click the link
    Then I should see user info "Welcome user2"
    When I hover over user 3 and click the link
    Then I should see user info "Welcome user3"
