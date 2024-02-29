from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):
    """
    :param context: Behave contextimport drive
    """
    # Install the Chrome WebDriver and get the driver path
    driver_path = ChromeDriverManager().install()
    # Create a service object for the Chrome WebDriver
    service = Service(driver_path)
    # Initialize the Chrome browser instance with the service
    context.driver = webdriver.Chrome(service=service)
    # Maximize the browser window
    context.driver.maximize_window()
    # Set implicit wait time for the driver
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 5)


def before_scenario(context, scenario):
    # Print the name of the scenario before it starts
    print('\nStarted scenario: ', scenario.name)
    # Initialize the browser for the scenario
    browser_init(context)


def before_step(context, step):
    # Print the name of the step before it starts
    print('\nStarted step: ', step)


def after_step(context, step):
    # Check if the step failed and print a message if it did
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, step):
    # Delete all cookies and quit
    context.driver.delete_all_cookies()
    context.driver.quit()
