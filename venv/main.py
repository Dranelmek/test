import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger()

token = os.getenv('TOKEN')
client = discord.Client()

def find_channel():
  text_channel_list = []
  for guild in client.guilds:
    for channel in guild.text_channels:
      text_channel_list.append(channel)
  return text_channel_list

@client.event
async def on_ready():
  print("starting as {0.user}".format(client))
  channels = find_channel()
  await channels[0].send('dramatic entry :boom:')


@client.event
async def on_message(message):
  channels = find_channel()
  if message.author == client.user:
    return
  if message.content.startswith("%hello"):
    await message.channel.send("HI!")
  elif message.content.startswith("%test"):
    await message.channel.send(":pensive:")
  elif message.content.startswith("%doit"):
    await message.channel.send("say less :muscle:")
    await channels[1].send("*neko")



client.run(token)