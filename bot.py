import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


token = os.environ["DISCORD_TOKEN"]
prefix = os.environ["PREFIX"]
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)
bot = commands.Bot(command_prefix=prefix, intents=intents,
                   activity=discord.Game("汎用Bot"), case_insensitive=True)
initial_extensions = ['cogs.omikuji']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


async def load_extension():
    for cog in initial_extensions:
        await bot.load_extension(cog)


async def main():
    async with bot:
        await load_extension()
        await bot.start(token)

asyncio.run(main())
