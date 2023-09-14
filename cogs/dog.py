import discord
from discord.ext import commands
import referances as ref
from discord import app_commands

class Dog(commands.Cog):
    def __init__(self, chu):
        self.chu = chu

    @app_commands.command(name= "dog", description="Dog Pictures")
    async def dog(self, interaction: discord.Interaction):
        await interaction.response.send_message(ref.get_dog()[0]['url'])


async def setup(chu):
    await chu.add_cog(Dog(chu))
