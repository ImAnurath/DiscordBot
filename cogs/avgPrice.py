import discord
from discord.ext import commands
import api_refs as ar
import requests
import json

class avgPrice(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Average', 'avg'])
    async def average(self, ctx, id):
        await ctx.send("Gimme a second!")
        r = requests.get(f"https://universalis.app/api/v2/history/Europe/{id}?entriesToReturn=10&minSalePrice=0&maxSalePrice=50000")
        data = json.loads(r.text)
        pricePerUnit = [entry["pricePerUnit"] for entry in data["entries"]]
        average_price = int(sum(pricePerUnit) / len(pricePerUnit))
        await ctx.send(f"Average Price: {average_price:,}.".replace(',','.'))


    
    

async def setup(chu):
    await chu.add_cog(avgPrice(chu))
