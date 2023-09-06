import discord
import requests
import json

def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.text)
    return data

def get_dog():
    response = requests.get("https://api.thedogapi.com/v1/images/search")
    data = json.loads(response.text)
    return data
def get_uni():
    response = requests.get("https://universalis.app/api/v2/data-centers")
    data = json.loads(response.text)
    return data