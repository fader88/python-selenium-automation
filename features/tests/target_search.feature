Feature: Search Test


  Scenario: User can search for the product
    Given Open Target.com
    When Search for Coffee
    Then Verify search result


  Scenario Outline: User can search for a product on target
    Given Open Target.com
    When Search for <search_word>
    Then Search results for <expected_result> are shown
    Then Page URL has search term <expected_part_url>
    Examples:
    |search_word    |expected_result    |expected_part_url    |
    |coffee mug     |coffee mug         |coffee+mug           |
    |coffee         |coffee             |coffee               |
    |tea            |tea                |tea                  |
