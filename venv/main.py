import discord

token = "OTQzMTY4NDY2OTYwMTUwNTY5.YgvIFQ.PUzV0Oct5bGpycNTdMdAzqKZ7Dk"
client = discord.Client()

@client.event
async def on_ready():
  print("starting as {0.user}".format(client))
  await message.channel.send("dramatic entry")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("%hello"):
    await message.channel.send("Hi!")

client.run(token)