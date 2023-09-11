import requests
import json
import os

r = requests.get(f"https://universalis.app/api/v2/Europe/39720?listings=1&fields=listings.pricePerUnit%2Clistings.worldName")
data = json.loads(r.text)
price = data["listings"][0]["pricePerUnit"]
server = data["listings"][0]["worldName"]
string = str(price) + " " + server
print(string)