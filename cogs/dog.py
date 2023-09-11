import nextcord
from nextcord.ext import commands
import referances as ref

class Dog(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Dog'])
    async def dog(self, ctx):
        await ctx.send(ref.get_dog()[0]['url'])


async def setup(chu):
    chu.add_cog(Dog(chu))
