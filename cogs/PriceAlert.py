import nextcord
from nextcord.ext import commands
import json
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)

class PriceAlert(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @commands.command(aliases=['palert'])
    async def PriceAlert(self, ctx, *args):
        name = " ".join(args)
        if name in itemNames:
            await ctx.send(itemNames[name])
        else:
            # Find the most similar item name
            item_name, score = process.extractOne(name, itemNames.keys())
            similarity_threshold = 90
            if score >= similarity_threshold:
                await ctx.send(f"Did you mean '{item_name}'?")
            else:
                await ctx.send("Item not found. Check your damn spelling.")
            
        
            

async def setup(chu):
    chu.add_cog(PriceAlert(chu))
