from datetime import datetime
import nextcord
from nextcord.ext import commands
import referances as ref
import requests
import json

embed = nextcord.Embed(
        title="Average Potion Prices",
        colour=0xc000f5,
        timestamp=datetime.now()
    )
idList = { 
                "Grade 8 Tincture of Strength" :39727, 
                "Grade 8 Tincture of Dexterity" :39728,
                "Grade 8 Tincture of Intelligence" :39730,
                "Grade 8 Tincture of Mind" :39731
                }


class Potion(commands.Cog):
    
    def __init__(self, chu):
        self.chu = chu
    
    @commands.command(aliases=['pot', 'potion'])
    async def Potion(self, ctx):
        await ctx.send("Gimme a second!")
        user = ctx.author
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text="Check time")
        average_prices = {}
        for item_name, item_id in idList.items():  # Calculates the average price
            r = requests.get(f"https://universalis.app/api/v2/history/Europe/{item_id}?entriesToReturn=10&minSalePrice=0&maxSalePrice=50000")
            data = json.loads(r.text)
            pricePerUnit = [entry["pricePerUnit"] for entry in data["entries"]]
            average_price = int(sum(pricePerUnit) / len(pricePerUnit))
            average_prices[item_name] = average_price
        for item_name, price in average_prices.items(): # Put the name of the item and prices into embed message
            embed.add_field(name=item_name, value=f"{price} gil", inline=False)
        await ctx.send(embed=embed)
        average_prices.clear()
        embed.clear_fields()

async def setup(chu):
    chu.add_cog(Potion(chu))



# + "https://universalis-ffxiv.github.io/universalis-assets/icon2x/39730.png"