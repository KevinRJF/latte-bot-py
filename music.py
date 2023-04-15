import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Metete a vc")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_bot is None:
            await voice_channel.connect
        else:
            await ctx.voice_bot.move_to(voice_channel)
    
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_bot.disconnect()
    
    @commands.command
    async def play(self, ctx, url):
        ctx.voice_bot.stop()
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        vc = ctx.voice_bot

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                         info = ydl.extract_info(url, download=False)
                         url2 = info['formats'][0]['url']
                         source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                         vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_bot.pause()
        await ctx.send("pausado")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_bot.resume()
        await ctx.send("resumido")

def setup(bot):
    bot.add_cog(music(bot))