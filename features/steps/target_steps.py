from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open Target.com')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    #context.driver.wait.until(EC.visibility_of_element_located(HEADER))
    context.app.main_page.open_main()


@when('Search for Coffee')
def search_coffe(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    context.driver.implicitly_wait(4)


@when('Search for huggies baby wipes')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('huggies baby wipes')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@when('Add product to the cart')
def open_cart(context):
    element = context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor13954318')
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    context.wait()


@when('Open the cart')
def open_cart(context):
    context.app.header.click_cart_icon()



@when('View cart')
def open_cart(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    context.wait()


@when('Click on Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


@when('Open Sign In form')
def open_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Verify search result')
def verify_search_results_correct(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_text, f'Expected word coffee not in {actual_text}'
    print('Test case passed')


@then('Verify cart is empty')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()

@then('Verify Sign In form displayed')
def verify_page(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
    print('Test case passed')


@then('Verify product in the cart')
def verify_product_in_cart(context):
    expected_result = "Huggies Natural Care Sensitive Unscented Baby Wipes - 168ct"
    actual_result = context.driver.find_element(By.XPATH, "//div[text()='Huggies Natural Care Sensitive Unscented "
                                                          "Baby Wipes - 168ct']").text
    assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)