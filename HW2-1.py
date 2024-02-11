from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# xpath to amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# ID of email field
driver.find_element(By.ID, 'ap_email')

# ID of continue button
driver.find_element(By.ID, 'continue')

# text() search of terms and conditions link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# text() search of privacy policy link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# xpath search of need help? link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# page does not contain the following elemnts: Forgot your password link & Other issues with Sign-In link

# ID of create your amazon account
driver.find_element(By.ID, 'createAccountSubmit')


print('elements are present')
driver.quit()

