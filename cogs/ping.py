from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        latency = round(self.chu.latency * 1000)
        await ctx.send(latency)


async def setup(chu):
    chu.add_cog(Ping(chu))
