# Created by sam at 2/13/24
Feature: Target cart test

  Scenario: Targe cart is empty
    Given Open Target.com
    When Open the cart
    Then Verify cart is empty