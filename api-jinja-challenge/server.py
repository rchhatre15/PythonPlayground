from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)

@app.route("/<name>")
def load(name):
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    print("gender",gender_response)
    gender = gender_response.json()['gender']
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age = age_response.json()['age']
    return render_template("index.html", name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)