import discord
from discord.ext import commands
import referances as ref
from datetime import datetime

embed = discord.Embed(
        colour=0xc000f5,
        timestamp= datetime.now()
    )
#embed.set_author(name="Universalis Data", icon_url="https://universalis.app/i/universalis/universalis.png")
embed.set_footer(text="Check time")
#embed.set_thumbnail(url=user.display_avatar.url)
class avgPrice(commands.Cog):
    
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Average', 'avg'])
    async def average(self, ctx, *args):
        itemName = " ".join(args)
        await ctx.send("Gimme a second!")
        data = ref.getAverage(itemName)
        embed.set_thumbnail(url=ref.getImageUrl(itemName))
        embed.add_field(name=itemName, value=f"{data} gil", inline=False)
        cheapest = ref.getCheapest(itemName)
        embed.add_field(name="Cheapest", value=f"{cheapest}", inline=False)
        await ctx.send(embed=embed)
        embed.clear_fields()

async def setup(chu):
    await chu.add_cog(avgPrice(chu))
