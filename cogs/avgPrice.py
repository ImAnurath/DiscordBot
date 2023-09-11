import discord
from discord.ext import commands
import referances as ref
import requests
import json
import os


class avgPrice(commands.Cog):
    
    def __init__(self, chu):
        self.chu = chu
    @commands.command(aliases=['Average', 'avg'])
    async def average(self, ctx, *args):
        name = " ".join(args)
        await ctx.send("Gimme a second!")
        data = ref.getAverage(name)
        await ctx.send(data)

async def setup(chu):
    await chu.add_cog(avgPrice(chu))
