import discord
from discord.ext import commands


token = "OTQzMTY4NDY2OTYwMTUwNTY5.YgvIFQ.qzxs7tRn4Jq6UwgXrVlEMOkBx3Q"
client = discord.Client()

@client.event
async def on_ready():
  print("starting as {0.user}".format(client))

bot = commands.Bot(command_prefix='$')

@bot.command(name='bro')
async def bro(ctx, arg):
    await ctx.send(arg)

# bot.add_command(bro)
client.run(token)