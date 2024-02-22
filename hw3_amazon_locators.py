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

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo[role='img'][aria-label='Amazon']")

driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

driver.find_element(By.ID, "ap_customer_name")

driver.find_element(By.ID, "ap_email")

driver.find_element(By.ID, "ap_password")

driver.find_element(By.CSS_SELECTOR, ".a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini")

driver.find_element(By.ID, "ap_password_check")

driver.find_element(By.ID, "auth-continue")

(By.CSS_SELECTOR, "a[href*='notification_condition_of_use']")

(By.CSS_SELECTOR, "a[href*='=ap_signin_notification_privacy_notice']")

(By.CSS_SELECTOR, "a[href='/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&prevRID=JK9C2E9899S8WK7T2VES&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")