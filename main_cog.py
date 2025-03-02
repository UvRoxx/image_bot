import discord
from discord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
જય જીનેન્દ્ર
General commands:
-help - displays all the available commands
Music commands:
-play <keywords> - finds the song on youtube and plays it in your current channel
-queue - displays the current music queue
-skip - skips the current song being played
Respect commands:
-jetha
BigPP commands:
-link <video_name>
-naughty <pic_name>
Meme commands:
-meme
-yomama
Lyrics And Recommendation
-rec <artist_name> Recommendation
-ly <song_name> by <artist_name> Lyrics
-recp <artist_name> Auto Play 5 Songs from Popular songs by Artist
-shzp <song_query> Auto Play Top Songs related to the query
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Clears a specified amount of messages")
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)

    @commands.command(name="jetha", help="Respect")
    async def jetha(self, ctx):
        await ctx.send("Chup Chutiye...")



