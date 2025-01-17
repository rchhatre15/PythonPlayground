from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def scrape_linkedin_job(driver, job_url):
    # LinkedIn login credentials - you should store these securely
    EMAIL = "rchhatre15@gmail.com"
    PASSWORD = "Ratel_patel15"

    # First go to LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Login
    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    
    # Wait for login to complete
    time.sleep(5)

    # Now navigate to the job URL
    driver.get(job_url)
    time.sleep(3)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
    i = 0
    for job in jobs:
        if i >= 3:
            break
        job.click()
        # try:
        #     save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        #     save.click()
        # except:
        #     jobs = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")[i:]
        time.sleep(2)
        save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save.click()
        i += 1



        


scrape_linkedin_job(driver, "https://www.linkedin.com/jobs/search/?currentJobId=4055357120&f_LF=f_AL&f_WT=2&geoId=106413121&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
