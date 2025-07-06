#use selenium AI automated test to test login page
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#setting chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
 

#

#start the webdriver with service and options
# Set up the ChromeDriver service correctly
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
#url of app
url = "http://127.0.0.1:5000"
#test case 1 :valid login
driver.get(url)
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(1)

message = driver.find_element(By.TAG_NAME, "p").text
if "Login successful" in message:
    print(" Valid login test passed")
else:
    print("❌ Valid login test failed")  
#save screenshot
driver.save_screenshot("login_success__test_result.png")    

#test case 2: Invalid login
driver.get(url)
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("wronguser")
driver.find_element(By.NAME, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(1)

message = driver.find_element(By.TAG_NAME, "p").text
if "Invalid credentials" in message:
    print("Invalid login test passed")
else:
    print("❌ Invalid login test failed")    

#save screenshot
driver.save_screenshot("login_test_result.png") 
driver.quit()   
# Note: Ensure the Flask app is running before executing this test script.
# This script uses Selenium to automate the login process and validate the functionality of the login page.
# The script tests both valid and invalid login scenarios and captures the results.# It also saves a screenshot of the test results for further analysis.
# Make sure to have the Flask app running locally on port 5000 before executing this script.
# The script uses ChromeDriverManager to manage the ChromeDriver installation automatically.
#clean up
import os
if os.path.exists("login_test_result.png"):
    os.remove("login_test_result.png")
    print("Screenshot cleaned up.")

'''
Task 2 Summary
In this task, I created a simple login page using Flask and tested it using Selenium.
The test script automated two scenarios: one with valid credentials (admin / 1234) and one with invalid credentials. 
It checked the result messages and printed whether each test passed or failed. A screenshot was also saved.
While this used basic Selenium, AI-powered tools could improve it by adapting to UI changes, 
suggesting new test cases, and reducing maintenance. 
This shows how automation and AI can make testing faster and more reliable.
'''