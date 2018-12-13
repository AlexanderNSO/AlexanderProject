# Created by tester at 11.12.2018
Feature: Authorize

  Scenario: Authorize new selfcare
    Given I open WebPage
    When i Filled in the authorization form
    Then i clicked auth button