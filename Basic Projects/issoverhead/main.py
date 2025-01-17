import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 39.042370 # Your latitude
MY_LONG = -77.487244 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
close = abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4
if sunset < 0:
    sunset = 24 + sunset


time_now = datetime.now()
print(sunrise)
print(sunset)
now = int(time_now.now().strftime("%H:%M:%S").split(":")[0])

# If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    if close and (now > sunset or now < sunrise):
        email = "thetempotester@gmail.com"
        password = "qcqolezcfkapsfqn"
        dest = "rchhatre15@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=dest,
                msg="Subject:ISS\n\nThe ISS is currently visible in Ashburn"
            )

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



