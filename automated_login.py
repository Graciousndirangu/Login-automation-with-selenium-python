from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

#variables for login credentials
username = "Your username or email address"
password = "Your password"



service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


#launch the browser and open url
driver.get("add_url")

#Find the username/email field and send the username to the input field.
uname = driver.find_element("id", "login_field")
uname.send_keys("username/email")

#Find the password input field and send the password to the input
pword = driver.find_element("id","password")
pword.send_keys("password")

# Click sign in button to login the website.
driver.find_element("name", "commit").click()
# Wait for login process to complete. 
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

#Verify that the login was successful.
error_message = "incorrect username or password!"

#Retrieve any errors found.
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

# When errors are found, log in fails
if any(error_message in e.text for e in errors):
	print("[!] Login Failed")
else:
	print("[+] Login successful")

time.sleep(10)
#close the driver
driver.close()


