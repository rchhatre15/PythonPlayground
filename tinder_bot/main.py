from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(5)

all_buttons = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
accept_cookies = all_buttons[3]
accept_cookies.click()

time.sleep(2)

all_buttons = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
login = all_buttons[2]
login.click()

time.sleep(2)

fb_login = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

EMAIL = os.getenv("FACEBOOK_EMAIL")
PASSWORD = os.getenv("FACEBOOK_PASSWORD")

email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)

time.sleep(5)

contin = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div')
contin.click()

driver.switch_to.window(base_window)

time.sleep(5)

all_buttons = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
allow = all_buttons[0]
allow.click()

time.sleep(2)

ignore = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/div[2]')
ignore.click()

time.sleep(5)

nah = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
nah.click()

time.sleep(2)

like = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div/main/div/div/div/div/div[5]/div/div[4]/button/span/span[1]')
# implement algorithm for auto liking/disliking
