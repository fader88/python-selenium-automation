from selenium.webdriver.common.by import By
from behave import given, when, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.product_number = product_id
    context.driver.get(f'https://www.target.com/p/{product_id}')
    context.driver.implicitly_wait(4)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = [
        ['Black', 'Brown', 'Cream', 'Dark Grey', 'Gree', 'Tan', 'Light Green'],
        ['Blue Tint', 'Denim Blue', 'Marine', 'Raven'],
        ['Black', 'Deep Olive', 'White']
    ]
    actual_colors = []
    if context.product_number == 'A-88063497':
        context.product_number = 0
    elif context.product_number == 'A-54551690':
        context.product_number = 1
    elif context.product_number == 'A-81540287':
        context.product_number = 2

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        selected_color = selected_color.split('\n')[1]  # Black
        actual_colors.append(selected_color)

    print(actual_colors)

    assert expected_colors[context.product_number] == actual_colors, \
        f'Expected {expected_colors[context.product_number]} did not match actual {actual_colors}'
