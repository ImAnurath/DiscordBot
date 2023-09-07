import discord
from discord.ext import commands
import api_refs as ar
import requests
import json

class Potion(commands.Cog):
    
    def __init__(self, chu):
        self.chu = chu
    

    @commands.command(aliases=['pot', 'potion'])
    async def Potion(self, ctx):
        await ctx.send("Gimme a second!")
        average_prices = {}
        idList = { 
                "Strength" :39727, 
                "Dexterity" :39728,
                "Intelligence" :39730,
                "Mind" :39731
                }
        for item_name, item_id in idList.items():
            r = requests.get(f"https://universalis.app/api/v2/history/Europe/{item_id}?entriesToReturn=10&minSalePrice=0&maxSalePrice=50000")
            data = json.loads(r.text)
            pricePerUnit = [entry["pricePerUnit"] for entry in data["entries"]]
            average_price = int(sum(pricePerUnit) / len(pricePerUnit))
            average_prices[item_name] = average_price
        response_message = "\n".join([f"Avg Price for {item}: {price} gil" for item, price in average_prices.items()])
        await ctx.send(response_message)
        
async def setup(chu):
    await chu.add_cog(Potion(chu))
