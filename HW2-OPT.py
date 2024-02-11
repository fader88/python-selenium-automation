from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
search_word = 'Toys'

driver.find_element(By.ID, 'search').send_keys(search_word)

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)

actual_text = driver.find_element(By.XPATH, "//div[@class='styles__HeadingContainer-sc-4tej7h-0 bFPZgY']").text
assert search_word in actual_text, f'Expected word {search_word} not in {actual_text}'

print('Test case passed')
driver.quit()