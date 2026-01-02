import smtplib
import datetime as dt
import random

# ------------------ CONSTANTS ------------------ #
MY_EMAIL = "abcs@gmail.com" #Gmail id
PASSWORD = "YOUR_APP_PASSWORD"   # Gmail App Password

# ------------------ QUOTES ------------------ #
with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

# ------------------ DATE ------------------ #
now = dt.datetime.now()
today = now.weekday()

# ------------------ WEEKLY EMAIL ------------------ #
WEEKLY_DAY = 0   # 0 = Monday (change if needed)

if today == WEEKLY_DAY:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="receiver_email@gmail.com",
            msg=f"Subject: Weekly Motivation 💪\n\n{quote}"
        )
    print("Weekly quote sent successfully!")
else:
    print("Today is not the scheduled day.")
