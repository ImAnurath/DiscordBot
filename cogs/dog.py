import discord
from discord.ext import commands
import api_refs as ar

class Dog(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Dog'])
    async def dog(self, ctx):
        await ctx.send(ar.get_dog()[0]['url'])


async def setup(chu):
    await chu.add_cog(Dog(chu))
