import discord
from discord.ext import commands
import api_refs as ar

class Cat(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command()
    async def cat(self, ctx):
        await ctx.send(ar.get_cat()[0]['url'])


async def setup(chu):
    await chu.add_cog(Cat(chu))
