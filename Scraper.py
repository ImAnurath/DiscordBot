import requests
from bs4 import BeautifulSoup
import json
import os 
import re
json_file_path = os.path.join(os.getcwd(), 'json', 'items.json') #To the pathing problems 

with open(json_file_path, 'r') as file: #Opens the json file
    item_ids = json.load(file)

item_names = {}

for item_id in item_ids:
    url = f"https://universalis.app/market/{item_id}"

    response = requests.get(url) #Website in HTML is now stored in response
    

    if response.status_code == 200: # Got this from AI. But it checks for if the request was successful?


        soup = BeautifulSoup(response.text, 'html.parser') # Got no fucking clue about this one. :')
        item_name_element = soup.find('div', class_="item_info").h1 # Directly find the location of a class. 


        item_name = item_name_element.get_text(strip=True) #Gets the div as a text first, strips it from white space

        # Regular expression to remove the leading digits. ^ = Means to match everything after it - \d = means digits [0-9] - + = more than 1. After every match(digit in this case) it finds in the item_name it will replace it with empty string
        result_string = re.sub(r"^\d+", "", item_name)

        item_names[item_id] = result_string


        print(f"{item_id}:{result_string} Has been added to the list")
    else:
        print(f"Failed to retrieve data for item ID {item_id}")

try: #Its already taking way too long. Just so that the code wont get fucked mid way :')
   
    with open(json_file_path, 'w') as file: # This is to write the retrieved names into the json file
        json.dump(item_names, file)
    print("Item names saved to items.json")
except Exception as e:
    
    print(f"Failed to save item names to items.json: {e}")
    
print("Item names saved to items.json")
