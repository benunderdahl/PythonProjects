from datetime import datetime as dt
import pandas as pd
import random
import smtplib

##################### Extra Hard Starting Project ######################
# port = 587
email =
password =
#
# # 1. Update the birthdays.csv
# data = pd.read_csv("birthdays.csv")
# print(data["name"])
# # 2. Check if today matches a birthday in the birthdays.csv
# now = dt.now()
# weekday = now.weekday()
# rand_num = random.randint(1,3)
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# for _, row in data.iterrows():
#     if int(row["month"]) == 9 and int(row["day"]) == 3:
#         with open(f"letter_templates/letter_{rand_num}.txt") as file:
#             letter = file.read()
#             letter = letter.replace("[NAME]", str(row["name"]))
#         with smtplib.SMTP("smtp.gmail.com", port) as conn:
#             conn.starttls()
#             conn.login(email, password)
#             conn.sendmail(email, row["email"], msg=f"Subject: Happy birfday\n\n{letter}")
# # 4. Send the letter generated in step 3 to that person's email address.
#
#
quotes = []
port = 587
email = ("")
with open("quotes.txt", "r") as file:
    data = file.readlines()
    for quote in data:
        quotes.append(quote.strip())


with smtplib.SMTP("smtp.gmail.com", port) as conn:
    conn.starttls()
    conn.login(email, password)
    conn.sendmail(email, "", msg=f"Subject: Daily Inspiration\n\n{random.choice(quotes)}")



