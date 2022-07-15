import discord
from discord.ext import commands
from core.classes import Cog_Extension

import json

with open('setting.json', mode='r', encoding='utf8' ) as setfile:  
    #mode = r means that the mode is read
    setdata = json.load(setfile)



class event(Cog_Extension) :

    @commands.Cog.listener() 
    async def on_member_join(self, member):
        channel=self.bot.get_channel( int(setdata['WELCOME_CHANNEL']) )
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel=self.bot.get_channel( int(setdata['LEAVE_CHANNEL']) )
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword=['peanuts', 'peanut', 'PEANUT', 'PPNUTS', 'NUTS']

        if msg.content in keyword : 
            await msg.channel.send('WAKU~~~~')

        elif msg.content=='study':
            await msg.channel.send('Anya go to sleep')
        
        elif msg.content.endswith('weak'):
            await msg.channel.send('you pretend WEAK')

        
    
    


def setup(bot):
    bot.add_cog(event(bot))