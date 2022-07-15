import discord
from discord.ext import commands
from core.classes import Cog_Extension # IDK why this line have a bug but anyway

import json

with open('setting.json', mode='r', encoding='utf8' ) as setfile:  
    #mode = r means that the mode is read
    setdata = json.load(setfile)



class react(Cog_Extension):

    @commands.command()
    async def 花生(self, ctx):
        pic = discord.File(setdata['pic'])
        #discord.File F must Capital F
        await ctx.send(file=pic)

    @commands.command()
    async def HI(self, ctx):
        await ctx.send('waku waku ')


def setup(bot):
    bot.add_cog(react(bot))