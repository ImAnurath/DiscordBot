import discord
from discord.ext import commands
import json
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from discord import app_commands
import referances as ref
from datetime import datetime


json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)
embed = discord.Embed(
        colour=0xc000f5,
        timestamp= datetime.now()
    )
embed.set_footer(text="Check time")

class AveragePrice(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "average_price", description="Returns average price of the item")
    async def averagePrice(self, interaction: discord.Interaction, itemName:str):
        await interaction.channel.send("avg test")
        itemName = itemName.title()
        await interaction.channel.send("Gimme a second!")
        if itemName in itemNames:
            data = ref.getAverage(itemName)
            embed.set_thumbnail(url=ref.getImageUrl(itemName))
            embed.add_field(name=itemName, value=f"{data} gil", inline=False)
            cheapest = ref.getCheapest(itemName)
            cheap = cheapest["listings"][0]["pricePerUnit"]
            server = cheapest["listings"][0]["worldName"]
            embed.add_field(name= "Cheapest", value=f"Price: {cheap} \n Server: {server}")
            await interaction.response.send_message(embed=embed)
        else:
            item_name, score = process.extractOne(itemName,itemNames.keys())
            similarity_threshold = 90
            if score >= similarity_threshold:
                await interaction.response.send_message(f"Did you mean '{item_name}'?")
            else:
                await interaction.response.send_message("Item not found. Check your damn spelling.")
        embed.clear_fields()

async def setup(chu):
    await chu.add_cog(AveragePrice(chu))
