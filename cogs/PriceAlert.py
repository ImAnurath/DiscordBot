import discord
from discord.ext import commands
import json
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from discord import app_commands
import referances as ref
import asyncio
from datetime import datetime

json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)
embed = discord.Embed(
        colour=0xc000f5,
        timestamp= datetime.now()
    )
embed.set_footer(text="Check time")

class PriceAlert(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "price_alert", description="Enter the name of the item and the price you want")
    async def priceAlert(self, interaction: discord.Interaction, name:str, price:int):
        name = name.title()
        embed.set_thumbnail(url=ref.getImageUrl(name))
        if name in itemNames:
            await interaction.channel.send(f"Alarm for {name} is set to {price} gil")
            while True:
                data = ref.getCheapest(name)
                unitPrice = data["listings"][0]["pricePerUnit"]
                server = data["listings"][0]["worldName"]
                if(unitPrice <= price):
                    embed.add_field(name=name, value=f"{unitPrice} gil \nServer: {server}", inline=False)
                    user = interaction.user.mention
                    await interaction.channel.send(f"{user}", embed=embed)
                    break
                else:
                    print("Waiting for 5 minutes")
                    await asyncio.sleep(300) #sleep for 5 min
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
