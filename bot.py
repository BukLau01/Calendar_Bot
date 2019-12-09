import asyncio
import discord
from discord.ext import commands

token = 'NjUyNzA1NTYyODA2NDUyMjM0.XesVrA.YjeYj8aOIGkJ5ZiPbghaOdz7mdU'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def test(ctx):
  await ctx.send("Hello World!")

bot.run(token)