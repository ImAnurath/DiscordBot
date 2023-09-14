import discord
from discord.ext import commands
import referances as ref
from discord import app_commands

class Cat(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "cat", description="Cat Pictures")
    async def cat(self, interaction: discord.Interaction):
        await interaction.response.send_message(ref.get_cat()[0]['url'])


async def setup(chu):
    await chu.add_cog(Cat(chu))
