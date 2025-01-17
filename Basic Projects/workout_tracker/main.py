import datetime

import requests
from datetime import *

api_key = "fc33b5b7a4fa07cbb76e53ebbe4bab40"
app_id = "1cd733f4"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "MALE"
WEIGHT_KG = "60.3"
HEIGHT = "172.7"
AGE = "20"

text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)


spreadsheet = "https://api.sheety.co/402ba88f3d39f1b6cae992763ad0200e/myWorkoutsProject/workouts"

new_header = {
    "Authorization": "Basic cmNoaGF0cmU6Z2V0bWVpbg=="
}
for exercise in result['exercises']:
    new_params = {
        "workout": {
            "date": date.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": str(exercise['name']).title(),
            "duration": str(exercise['duration_min']).title(),
            "calories": str(exercise["nf_calories"]).title()
        }
    }

    new_response = requests.post(url=spreadsheet, json=new_params, headers=new_header)
    print(new_response)
