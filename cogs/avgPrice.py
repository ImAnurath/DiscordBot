import discord
from discord.ext import commands
import referances as ref
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json
import os
json_file_path = os.path.join(os.getcwd(), 'json', 'itemNames.json')
with open(json_file_path, 'r') as file:
    itemNames = json.load(file)


embed = discord.Embed(
        colour=0xc000f5,
        timestamp= datetime.now()
    )
embed.set_footer(text="Check time")
class avgPrice(commands.Cog):
    
    def __init__(self, chu):
        self.chu = chu
    
    @commands.command(aliases=['Average', 'avg'])
    async def average(self, ctx, *args):
        itemName = " ".join(args)
        await ctx.send("Gimme a second!")
        
        if itemName in itemNames:
            data = ref.getAverage(itemName)
            embed.set_thumbnail(url=ref.getImageUrl(itemName))
            embed.add_field(name=itemName, value=f"{data} gil", inline=False)
            cheapest = ref.getCheapest(itemName)
            embed.add_field(name="Cheapest", value=f"{cheapest}", inline=False)
            await ctx.send(embed=embed)
        else:
            item_name, score = process.extractOne(itemName, itemNames.keys())
            similarity_threshold = 90
            if score >= similarity_threshold:
                await ctx.send(f"Did you mean '{item_name}'?")
            else:
                await ctx.send("Item not found. Check your damn spelling.")
        embed.clear_fields()

async def setup(chu):
    await chu.add_cog(avgPrice(chu))
