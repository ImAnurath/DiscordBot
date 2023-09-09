import discord
from discord.ext import commands


class PriceAlert(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.PriceAlert(aliases=['palert'])
    async def PriceAlert(self, ctx, id):
        
        


async def setup(chu):
    await chu.add_cog(PriceAlert(chu))
