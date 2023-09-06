import discord
from discord.ext import commands
import requests
import json
import api_refs as ar
import os
import asyncio

#config = json.loads(open("json/config.json").read())
#TOKEN = config["settings"]["token"]

TOKEN = "token"
chu = commands.Bot(command_prefix = "!", intents= discord.Intents().all())

@chu.event
async def on_ready():
    print("Logged in as {0.user}".format(chu))



@chu.command()
async def uniImage(self, ctx, arg):
    embed = discord.Embed(title= "Item ID: {arg}", url= "https://universalis-ffxiv.github.io/universalis-assets/icon2x/{arg}.png" )
    await ctx.send(embed)
@chu.command()
async def uniTest(ctx):
    r = requests.get("https://universalis.app/api/v2/Europe/39720")
    data = json.loads(r.text)
    newData = data["listings"]["itemID"]
    await ctx.send("Item ID: ", newData)





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