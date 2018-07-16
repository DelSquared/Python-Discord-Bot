import discord
from discord.ext import commands
from discord.utils import get
from discord import Client
import asyncio
import aiohttp
import numpy as np
import os

identity=str(np.genfromtxt("ID.txt", dtype=np.str,delimiter=","))
status=np.genfromtxt("Status.txt", dtype=np.str,delimiter=",")

bot=commands.Bot(command_prefix="%")

@bot.event
async def on_ready():
  r=int(np.random.uniform(0,len(status)))
  print("Test bot is on\n")
  await bot.change_presence(game=discord.Game(name=str(status[r])))

@bot.command(pass_context=True)
async def hello(ctx):
  print("hello")
  await bot.say("Hello :)")

@bot.command(pass_context=True)
async def refreshstatus(ctx):
  global status
  status=np.genfromtxt("Status.txt", dtype=np.str,delimiter=",")
  f=int(np.random.uniform(0,len(status)))
  await bot.change_presence(game=discord.Game(name=str(status[f])))
  await bot.say("status refreshed")


bot.run(identity) #The id code was drawn from an external txt file
