import requests
import smtplib

MY_EMAIL = "shammibajaj499@gmail.com"
MY_PASSWORD = "gqhc xtrq bmic sxik"

api_key = "0d7d0cef7ea1f441341188977a4f287b"
Api = 'https://api.openweathermap.org/data/2.5/forecast'
Parameters = {
    "lat": 10.607030,
    "lon": 78.417900,
    "appid": api_key
}

response = requests.get(Api, params=Parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Rain Alert\n\nIt's going to rain today. Remember to bring an umbrella."

        )


