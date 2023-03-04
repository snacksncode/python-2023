# pip install requests   #jak przy Faker
import requests

res = requests.get("http://worldtimeapi.org/api/timezone/Europe/Warsaw")
j = res.json()
print(j)
print(type(j))
print(j["day_of_week"])
