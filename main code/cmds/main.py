import discord
from discord.ext import commands
from core.classes import Cog_Extension



class main(Cog_Extension) :

    @commands.command()
    async def ping(self, ctx): #ctx means context including which server、channel and so on
        await ctx.send(f'{ round(self.bot.latency*1000) } (ms)') #change sec into msec

def setup(bot):
    bot.add_cog(main(bot))