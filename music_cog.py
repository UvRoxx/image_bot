import os
import random
from time import sleep
import discord
from discord.ext import commands
import lyricsgenius
import requests
from youtube_dl import YoutubeDL
import json
from porn_desi import search
from porn_parts import get_porn
from youtubemusic import YouTubeMusic


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.youtubeMusic = YouTubeMusic()
        # all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}

        self.YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True'}
        self.vc = ""

    # searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            # get the first url
            m_url = self.music_queue[0][0]['source']

            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegOpusAudio.from_probe(m_url, **self.FFMPEG_OPTIONS),
                         after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            # try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])

            print(self.music_queue)
            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play", help="Plays a selected song from youtube")
    async def p(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="queue", help="Displays the current songs in queue")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="skip", help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            # try to play next in the queue if it exists
            await self.play_music()

    @commands.command(name="link", help="Respect")
    async def porn(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            porn = get_porn(query=query, content='video')
            await ctx.send(f"Bhai Yeh Dekh {porn}")

    @commands.command(name="naughty", help="Respect")
    async def pic_porn(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            porn = get_porn(query=query, content='video')
            await ctx.send(f"Gazab Maal Hai{porn}")

    @commands.command(name="bobita", help="Respect")
    async def bobita(self, ctx):
        await ctx.send("Bhabhi Hai Rei Bobita Ji Bol BSDK...")

    @commands.command(name="p", help="Plays a selected song from youtube")
    async def pl(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="f", help="Respect")
    async def ff(self, ctx):
        await ctx.send("f")

    @commands.command(name="NoU", help="Respect")
    async def nou(self, ctx):
        await ctx.send("NoU")

    @commands.command(name="p", help="Plays a selected song from youtube")
    async def pl(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="boobita", help="Respect")
    async def porn(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            info = search(query)[0]
            porn = info['urls']
            preview = info['imgs']
            await ctx.send(f"Maza Aah Gaya {preview}\n{porn}")

    @commands.command(name="cc", help="Respect")
    async def cc_stop(self, ctx):
        if self.vc:
            self.vc.stop()
        await ctx.send("Kardiya Bapuji...")

    @commands.command(name="ban", help="Respect")
    async def ban(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            choice = random.randint(0, 100)
            if choice % 2 == 0:
                await ctx.send(f"Maaf kara {query} ko")
            else:
                await ctx.send(f"Ban Kar Sale ko...kick {query}")

    @commands.command(name="acneproblem", help="Respect")
    async def nou(self, ctx):
        await ctx.send("Chaliye Shuru Karte Hai...")
        query = 'https://www.youtube.com/watch?v=ljFT_RSEQYU'
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
            else:
                await ctx.send("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="artist", help="Respect")
    async def artist(self, ctx, *args):
        query = " ".join(args)
        genius = lyricsgenius.Genius(os.getenv("GENIUS"))
        artist = genius.search_artist(query, max_songs=5, sort="title")
        voice_channel = ctx.author.voice.channel
        songs = []
        for song in artist.songs:
            songs.append(song)
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            for song in songs:
                await ctx.send(f"{song}")
    # https://api.yomomma.info
    @commands.command(name="meme", help="Meme")
    async def meme(self, ctx):
        content = requests.get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(title=f"{data['title']}", Color=discord.Color.random()).set_image(url=f"{data['url']}")
        await ctx.reply(embed=meme)

    @commands.command(name="yomama", help="Yo Mama Meme")
    async def yomama(self, ctx):
        content = requests.get("https://api.yomomma.info").json()['joke']
        await ctx.send(content)

    @commands.command(name="l", help="Lyrics")
    async def ly(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            lyrics = await self.youtubeMusic.getLyrics(query)
            if lyrics:
                if len(lyrics['lyrics']) > 1800:
                    lyrics['lyrics'] = f'{lyrics["lyrics"][0: 1800]}\n...'
                    lyrics[
                        'source'] += '\nLyrics contain more than 2000 characters.\nUse lyricsSend to get them in a TXT file.'
                await self.embed.lyrics(
                    ctx,
                    lyrics,
                )
            else:
                await self.embed.exception(
                    ctx,
                    'Lyrics Not Found',
                    'Lyrics are not present for this track. 📖',
                    '❌'
                )