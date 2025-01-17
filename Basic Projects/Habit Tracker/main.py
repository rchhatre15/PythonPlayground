import requests
from datetime import *

site = "https://pixe.la/v1/users"
params = {
    "token": "gogginstate",
    "username": "rc",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=site, json=params)
# print(response.text)

graph_url = f"{site}/rc/graphs"
config = {
    "id": "graph1",
    "name": "fasting",
    "unit": "meals",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": "gogginstate"
}

# response = requests.post(url=graph_url, json=config, headers=headers)

pixel_url = f"{site}/rc/graphs/graph1"
pixel_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "1"
}

# response = requests.post(url=pixel_url, json=pixel_config, headers=headers)
# print(response.text)

new_site = f'{site}/rc/graphs/graph1/{datetime.now().strftime("%Y%m%d")}'
new_config = {
    "quantity": "4"
}
# response = requests.put(url=new_site, json=new_config, headers=headers)
# print(response.text)

response = requests.delete(url=new_site, json=new_config, headers=headers)
print(response.text)
