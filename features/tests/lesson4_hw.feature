Feature: Verify that elements are present at the page


  Scenario: Verify 5 benefits are displayed
    Given Open Circle page
    Then Verify 5 benefits are displayed


  Scenario Outline: Verify UI elements are present on the Help Page
    Given Open Help Page
    When Verify <element> present on the page
    Examples:
|element          |
|Header           |
|Search Field     |
|Search Button    |
|Common Issues    |
|All Help         |
|Contact & Recalls|
