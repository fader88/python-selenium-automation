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

# step 1 open the link
driver.get('https://www.target.com/')

# step 2 Click SignIn button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

# step 3 Click SignIn button in the side bar
driver.find_element(By.XPATH, "//a[@href='/account']").click()
sleep(6)

# step 4 Verify SignIn page opened
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
driver.find_element(By.XPATH, "//button[@type='submit']")

print('Test case passed')
driver.quit()
