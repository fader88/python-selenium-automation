Feature: Target test cases for the 3rd lesson


  Scenario: Targe cart is empty
    Given Open Target.com
    When Open the cart
    Then Verify cart is empty


  Scenario: Sign In form displayed
    Given Open Target.com
    When Click on Sign In
    And Open Sign In form
    Then Verify Sign In form displayed


  Scenario: Item added to the cart and displayed
    Given Open Target.com
    When Search for huggies baby wipes
    And Add product to the cart
    And View cart
    Then Verify product in the cart