import discord
from discord.ext import commands
import referances as ref
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "ping", description="Bot Latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.chu.latency * 1000)
        await interaction.response.send_message(f"Latency: {latency}ms")


async def setup(chu):
    await chu.add_cog(Ping(chu))
