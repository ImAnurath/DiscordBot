import discord
from discord.ext import commands
import json
import referances as ar
import os
import asyncio
import time

with open("actual/actual.json") as json_file:
    data = json.load(json_file)
TOKEN = data['settings']['token']

intents = discord.Intents.default()
intents.message_content = True

chu = commands.Bot(command_prefix= "!",intents= intents)

@chu.tree.command(name= "shutdown", description="Shuts Down the bot")
async def shutdown(interaction: discord.Interaction):
    await interaction.response.send_message("Shutting Down the Bot")
    await chu.close()

@chu.event
async def on_ready():
    print("Loading Cogs: ")
    synced = await chu.tree.sync()
    print(f"Number of Commands Synced {len(synced)}, Name: {synced}")
    print(f"Logged in as {chu.user}")

async def load():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await chu.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await chu.start(TOKEN)
asyncio.run(main())