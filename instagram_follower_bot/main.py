from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


class insta_follower:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.followers = []
        self.following = []
        self.username = None
        self.password = None
    
    def login(self, username, password):
        
        self.driver.get("https://www.instagram.com/")
        self.username = username
        self.password = password
        time.sleep(5)  # Wait for the login page to load
        
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        
        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        
        time.sleep(7)
        return


    def scrape_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(5)

        # Open the followers list
        followers_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
        followers_count = int(followers_link.text.split(" ")[0].replace(",", "").strip())
        print(f"Total followers to scrape: {followers_count}")
        followers_link.click()
        time.sleep(5)

        # Locate the scrollable popup using the provided XPath
        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        followers_data = set()
        last_scroll_height = 0
        retries = 0
        max_retries = 5

        while len(followers_data) < followers_count and retries < max_retries:
            # Extract followers
            html_content = scrollable_popup.get_attribute('innerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')

            followers_div_class = 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'
            username_span_class = '_ap3a _aaco _aacw _aacx _aad7 _aade'

            for follower_div in soup.find_all('div', class_=followers_div_class):
                try:
                    username = follower_div.find('span', class_=username_span_class).text.strip()
                    followers_data.add(username)
                except AttributeError:
                    continue

            print(f"Followers collected so far: {len(followers_data)}")

            # Scroll and check behavior
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            if retries == 3:
                time.sleep(10)
            else:
                time.sleep(1)

            new_scroll_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable_popup)
            if new_scroll_height == last_scroll_height:
                retries += 1
            else:
                retries = 0
            last_scroll_height = new_scroll_height

        if retries == max_retries:
            print("Stopped scrolling due to no new followers being loaded.")

        close_button = self.driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
        close_button.click()

        print(f"Total followers scraped: {len(followers_data)}")
        return list(followers_data)



    def scrape_following(self):
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(5)

        # Open the following list
        following_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]')
        following_count = int(following_link.text.split(" ")[0].replace(",", "").strip())
        print(f"Total following to scrape: {following_count}")
        following_link.click()
        time.sleep(5)

        # Locate the scrollable popup using the provided XPath
        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        following_data = set()
        last_scroll_height = 0
        retries = 0
        max_retries = 5

        while len(following_data) < following_count and retries < max_retries:
            # Extract following
            html_content = scrollable_popup.get_attribute('innerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')

            following_div_class = 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'
            username_span_class = '_ap3a _aaco _aacw _aacx _aad7 _aade'

            for following_div in soup.find_all('div', class_=following_div_class):
                try:
                    username = following_div.find('span', class_=username_span_class).text.strip()
                    following_data.add(username)
                except AttributeError:
                    continue

            print(f"Following collected so far: {len(following_data)}")

            # Scroll and check behavior
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            if retries == 3:
                time.sleep(10)
            else:
                time.sleep(1)

            new_scroll_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable_popup)
            if new_scroll_height == last_scroll_height:
                retries += 1
            else:
                retries = 0
            last_scroll_height = new_scroll_height

        if retries == max_retries:
            print("Stopped scrolling due to no new accounts being loaded.")

        close_button = self.driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
        close_button.click()

        print(f"Total following scraped: {len(following_data)}")
        return list(following_data)

    
    def identify_snakes(self):
        # Convert to sets for easier comparison
        followers_set = set(self.followers)
        following_set = set(self.following)

        # Find the difference
        snakes = following_set - followers_set

        print(f"Identified {len(snakes)} snakes (not following back).")

        # Save the snakes to a text file
        output_file_path = "instagram_follower_bot/snakes.txt"
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for snake in snakes:
                file.write(f"{snake}\n")

        print(f"Snakes saved to {output_file_path}.")
        return list(snakes)


snake_finder = insta_follower()
Username = ""
Password = ""
snake_finder.login(Username, Password)
snake_finder.followers = snake_finder.scrape_followers()
snake_finder.following = snake_finder.scrape_following()
snake_finder.identify_snakes()