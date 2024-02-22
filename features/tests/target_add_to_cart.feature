# Created by sam at 2/13/24
Feature: Target add item to the cart test

  Scenario: Item added to the cart and displayed
    Given Open Target.com
    When Search for huggies baby wipes
    And Add product to the cart
    And View cart
    Then Verify product in the cart
g