import discord
from discord.ext import commands
import logging

logger = logging.getLogger()

token = "OTQzMTY4NDY2OTYwMTUwNTY5.YgvIFQ.qzxs7tRn4Jq6UwgXrVlEMOkBx3Q"
client = discord.Client()

def find_channel():
  text_channel_list = []
  for server in discord.Client.servers:
    for channel in server.channels:
      if channel.type == 'Text':
        text_channel_list.append(channel)
  return text_channel_list

@client.event
async def on_ready():
  logger.debug("starting as {0.user}".format(client))
  id = find_channel()[0]
  channel = client.get_channel(id)
  await channel.send('Hello :wave:')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("%hello"):
    await message.channel.send("HI!")
  elif message.content.startswith("%test"):
    await message.channel.send(":pensive:")

client.run(token)