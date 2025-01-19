from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# 50 cookie factories, 5 cookie portals, 1 cookie portal, time machine 

cookie = driver.find_element(By.ID, "cookie")
factory_count = 0
factory_val = 500
portal_count = 0
portal_val = 1000000
time_machine_val = 123456789
import time
timeout = time.time() + 5  # 5 seconds from now
five_min_timeout = time.time() + 300  # 5 minutes from now

while True:
    try:
        cookie.click()
    except:
        print("click no work")
    
    # Check if 5 minutes have passed
    if time.time() > five_min_timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cps}")
        break
    
    # Check if 5 seconds have passed
    if time.time() > timeout:
        cookie = driver.find_element(By.ID, "cookie")
        money = driver.find_element(By.ID, "money").text
        factory = driver.find_element(By.ID, "buyFactory")
        portal = driver.find_element(By.ID, "buyPortal")
        time_machine = driver.find_element(By.ID, "buyTime machine")
        money = money.replace(",", "")
        if int(money) > factory_val and factory_count < 20:
            factory.click()
            factory_count += 1
            factory_val *= 1.15
        elif int(money) > portal_val and portal_count < 6:
            portal.click()
            portal_count += 1
            portal_val *= 1.15      
        elif int(money) > time_machine_val:
            time_machine.click()
            time_machine_val *= 1.15
            
        timeout = time.time() + 5  # Reset the timeout

driver.quit()
