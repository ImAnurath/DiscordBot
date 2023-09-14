import discord
from discord.ext import commands
import json
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from discord import app_commands
from typing import Tuple

json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)

class PriceAlert(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "price_alert", description="Enter the name of the item") # This command still needs to become an actual alert
    async def priceAlert(self, interaction: discord.Interaction, name:str):
        name = name.title()
        if name in itemNames:
            await interaction.response.send_message(itemNames[name])
        else:
            # Find the most similar item name
            item_name, score = process.extractOne(name, itemNames.keys())
            similarity_threshold = 90
            if score >= similarity_threshold:
                await interaction.response.send_message(f"Did you mean '{item_name}'?")
            else:
                await interaction.response.send_message("Item not found. Check your damn spelling.")
            
        
            

async def setup(chu):
    await chu.add_cog(PriceAlert(chu))
