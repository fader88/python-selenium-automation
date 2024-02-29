from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, '.custom-h2')
SEARCH_FIELD = (By.ID, 'j_id0:j_id2:j_id32:name')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[alt='search']")
COMMON_ISSUES = (By.CSS_SELECTOR, '.box-column')
ALL_HELP = (By.XPATH, "//h2[text()='Browse all Help pages']")


@given('Open Circle page')
def go_to_main(context):
    context.driver.get('https://www.target.com/circle')
    context.wait.until(...)


@given('Open Help Page')
def go_to_help(context):
    context.driver.get('https://help.target.com/help')
    context.wait.until(...)

@then('Verify 5 benefits are displayed')
def benefits_verification(context):
    expected_result = 5
    actual_result = context.driver.find_elements(By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
    assert len(actual_result) == expected_result, f'Expected {expected_result} but got {actual_result}'


@when('Verify {element} present on the page')
def help_ui_verification(context, element):
    if element == 'Header':
        actual_result = context.driver.find_element(*HEADER)
    elif element == 'Search Field':
        actual_result = context.driver.find_element(*SEARCH_FIELD)
    elif element == 'Search Button':
        actual_result = context.driver.find_element(*SEARCH_BUTTON)
    elif element == 'Common Issues':
        actual_result = context.driver.find_element(*COMMON_ISSUES)
    elif element == 'All Help':
        actual_result = context.driver.find_element(*ALL_HELP)
    elif element == 'Contact & Recalls':
        actual_result = context.driver.find_elements(By.CSS_SELECTOR, "[class*='boxSmallr']")
        expected_result = 2
        assert expected_result == len(context.driver.find_elements(By.CSS_SELECTOR, "[class*='boxSmallr']")), \
            f'Expected elements was not located'
    print(actual_result)
