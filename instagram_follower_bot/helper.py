from bs4 import BeautifulSoup
import json

# Your provided HTML
with open('html.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()
# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize a list to store followers' data
followers_data = []

# Extract relevant data
for follower in soup.find_all('div', class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'):  # Adjust class based on your actual structure
    try:
        username = follower.find('span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade').text.strip()
        
        # Append data to the list
        followers_data.append({
            'username': username,
        })
    except AttributeError:
        continue

# Convert to JSON
followers_json = json.dumps(followers_data, indent=4)

# Save to a file
with open('followers_data.json', 'w') as file:
    file.write(followers_json)

print(f"Extracted {len(followers_data)} followers:")
print(followers_json)
