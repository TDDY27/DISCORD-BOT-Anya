import discord
from discord.ext import commands

import json  #to save token or other things
import random 
import os

with open('setting.json', mode='r', encoding='utf8' ) as setfile:  
    #mode = r means that the mode is read
    setdata = json.load(setfile)


bot=commands.Bot(command_prefix='_')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{ filename[:-3] }')

if __name__=="__main__" :
    bot.run( setdata['TOKEN'] )