from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time 

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

# facebook = driver.find_element(By.XPATH, '"//*[contains(@aria-label, "Log in with Facebook")]"')
# facebook.click()
all_buttons = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
fb = all_buttons[3]
fb.click()

time.sleep(2)

main_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window:
        fb_popup = handle
        break

driver.switch_to.window(fb_popup)


EMAIL = "rchhatre15@gmail.com"
PASSWORD = "Ratel_patel15"
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)

time.sleep(5)

contin = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div')
contin.click()

driver.switch_to.window(main_window)

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



