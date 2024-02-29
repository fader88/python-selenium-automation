Feature: Tests for product page

  Scenario Outline: User can select colors
    Given Open target product <product_id> page
    Then Verify user can click through colors
    Examples:
    |product_id   |
    |A-88063497   |
    |A-54551690   |
    |A-81540287   |
