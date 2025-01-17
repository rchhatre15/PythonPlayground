import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
    msg = quotes[random.randint(0, len(quotes)-1)]

    email = "thetempotester@gmail.com"
    r_email = "thetempotester@yahoo.com"
    password = "qcqolezcfkapsfqn"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=r_email,
            msg=f"Subject:Project\n\n{msg}"
        )

