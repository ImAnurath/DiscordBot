import discord
from discord.ext import commands
import referances as ref

class Cat(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Cat'])
    async def cat(self, ctx):
        await ctx.send(ref.get_cat()[0]['url'])


async def setup(chu):
    chu.add_cog(Cat(chu))
