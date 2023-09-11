import requests
import json
import os

json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)

def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.text)
    return data
def get_dog():
    response = requests.get("https://api.thedogapi.com/v1/images/search")
    data = json.loads(response.text)
    return data
def getAverage(name):
    id = itemNames[name]
    r = requests.get(f"https://universalis.app/api/v2/Europe/{id}?listings=10&fields=listings.pricePerUnit")
    data = json.loads(r.text)
    prices = [item["pricePerUnit"] for item in data["listings"]]
    average_price = sum(prices) / len(prices)
    return int(average_price)
def getID(name):
    id = itemNames[name]
    return id
def getImageUrl(name):
    id = itemNames[name]
    return (f"https://universalis-ffxiv.github.io/universalis-assets/icon2x/{id}.png")
def getCheapest(name):
    id = itemNames[name]
    r = requests.get(f"https://universalis.app/api/v2/Europe/{id}?listings=1&fields=listings.pricePerUnit%2Clistings.worldName")
    data = json.loads(r.text)
    price = data["listings"][0]["pricePerUnit"]
    server = data["listings"][0]["worldName"]
    string = str(price) + " gil at " + server
    return string
    
