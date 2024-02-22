# Created by sam at 2/12/24
Feature: Search Test
  # Enter feature description here

  Scenario: User can search for the product
    Given Open Target.com
    When Search for Coffee
    Then Verify search result