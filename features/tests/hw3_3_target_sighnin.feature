# Created by sam at 2/13/24
Feature: Target Sign In form test
  # Enter feature description here

  Scenario: Sign In form displayed
    Given Open Target.com
    When Click on Sign In
    And Open Sign In form
    Then Verify Sign In form displayed