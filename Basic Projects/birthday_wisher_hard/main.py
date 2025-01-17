import smtplib
import datetime as dt
import random
import pandas
import csv


# 1. Update the birthdays.csv
column_name = ["Name", "email", "Year", "Month", "Day"]
data = [
    ["Umesh", "uchhatre@gmail.com", 1971, 5, 24],
    ["Rohit", "rchhatre29@gmail.com", 1999, 9, 5],
    ["Umesh", "uchhatre@gmail.com", 1973, 12, 6],
    ["God", "thetempotester@yahoo.com", 2003, 5, 20],
]
with open('birthdays.csv', 'w') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(column_name)
    writer.writerows(data)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

df = pandas.read_csv("birthdays.csv")
matches = []
for (index, row) in df.iterrows():
    if row.Month == month and row.Day == day:
        matches.append((row.Name, row.email))

print(matches)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
if len(matches) > 0:
    for name, email in matches:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as file:
            text = file.read()
        msg = text.replace("[NAME]", name)

        print(msg)

        mail = "thetempotester@gmail.com"
        password = "qcqolezcfkapsfqn"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mail, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Project\n\n{msg}"
            )






