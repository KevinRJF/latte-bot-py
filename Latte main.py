import discord
from discord.ext import commands
from transformers import pipeline
import random
import datetime
from urllib import parse, request
import re
import requests, json
import os
import yt_dlp
from yt_dlp import YoutubeDL
from discord import FFmpegPCMAudio
from ast import alias
import aiohttp
from requests import get
import asyncio
from pytube import YouTube
from moviepy import editor
import threading
from dotenv import load_dotenv
import youtube_search as YT
from discord.utils import get

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.is_playing = False
        self.is_paused = False
        
        self.vc = None
        self.music_queue = []
    
bot = commands.Bot(command_prefix=["lat ", "Lat "], intents=discord.Intents.all(), activity=discord.Game(name="Soy hija de KevinRJF"), case_insensitive=True)

#bot.load_extension("music")

#for i in range(len(cogs)):
#    cogs[i].setup(bot)

#class music(commands.Cog):
#    def __init__(self, bot):
#        self.bot = bot

@bot.event
async def on_ready():
    print(f"{bot.user} va sobre")

#################################################################################################################################################

class SupremeHelpCommand(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Lista de comandos", color=discord.Color.blurple())
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            if command_signatures := [
                self.get_command_signature(c) for c in filtered
            ]:
                cog_name = getattr(cog, "qualified_name", "Sin categorizar")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command) , color=discord.Color.blurple())
        if command.help:
            embed.description = command.help
        if alias := command.aliases:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_help_embed(self, title, description, commands): # esta es una helper function para agregar comandos en embed
        embed = discord.Embed(title=title, description=description or "No se encontró ayuda...")

        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                embed.add_field(name=self.get_command_signature(command), value=command.help or "No se encontró ayuda...")

        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        title = self.get_command_signature(group)
        await self.send_help_embed(title, group.help, group.commands)

    async def send_cog_help(self, cog):
        title = cog.qualified_name or "No"
        await self.send_help_embed(f'{title} Category', cog.description, cog.get_commands())

bot.help_command = SupremeHelpCommand()

################################################################################################################################################     

#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send(f"{ctx.author.mention} perdón no te entendí\n\n(In english: {(error)})\n\nPuedes escribir `lat help` para leer una lista de mis comandos actuales") 

#class SupremeHelpCommand(commands.HelpCommand):
#    async def send_error_message(self, error):
#        embed = discord.Embed(title="No te entendí xd", description=(f"In english: {(error)}"), color=discord.Color.red())
#        channel = self.get_destination()
#
#        await channel.send(embed=embed)

#@commands.command()
#async def shutdown(self,ctx):
#    if ctx.message.author.id == OWNERID: #replace OWNERID with your user id
#      print("shutdown")
#      try:
#        await self.bot.logout()
#      except:
#        print("EnvironmentError")
#        self.bot.clear()
#    else:
#       await ctx.send("You do not own this bot!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return

    if bot.user.mention == message.content and message.mention_everyone is False:
        await message.channel.send(f"Que onda {message.author.mention}")
    await bot.process_commands(message)

@bot.listen('on_message')
async def sadwords(message):
     if any(word in message.content for word in sad_words):
          await message.channel.send(random.choice(starter_happywords))

sad_words = ["triste", "depre", "deprimido", "infeliz", "suicidio", "suicidar", "suicidarme",
             "matarme", "colgarme"]

starter_happywords = [
     "Ánimos :muscle:",
     "Cada día es una nueva oportunidad para que cambiés tu vida",
     "Tu actitud, no tu aptitud, determinará tu altitud mi broder",
     "La vida tiene el color con el que vos la querrás pintar",
     "Enfrentá a tus miedos dale no seas cochón."]
     
#podés usar el comando `-help` para que te dé una lista de todos mis comandos actuales. :saluting_face: 

@bot.listen('on_message')
async def listenmsg(msg):
    if 'latte' in msg.content.lower():
        channel = msg.channel
        await channel.send(':woman_raising_hand:')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'i need to kill my enemies' in msg.content.lower():
        channel = msg.channel
        await channel.send('You have no enemies. No one in the world is your enemy. There is no one you need to hurt.')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'marine code' in msg.content.lower():
        channel = msg.channel
        await channel.send('**01746**\n\nhttps://tenor.com/68Es.gif')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'let him cook' in msg.content.lower():
        channel = msg.channel
        await channel.send('https://tenor.com/b0oe8.gif')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'pato' in msg.content.lower():
        channel = msg.channel
        await channel.send('https://tenor.com/boioN.gif')


@bot.listen('on_message')
async def listenmsg(msg):
    if 'mamala chebin' in msg.content.lower():
        channel = msg.channel
        await channel.send('sos cochón chebin')

@bot.listen('on_message')
async def listenmsg(message):
        if message.author == bot.user:
            return
        if message.author.bot: return
        if 'sex' in message.content.lower():
            channel = message.channel
            await channel.send('https://media.discordapp.net/attachments/522820942125203462/897435255605198858/885398144244928524.gif?width=160&height=160')


#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if message.author.bot: return

#    if bot.user.mention == message.content and message.mention_everyone is False:
#        await message.channel.send(f"Que onda {message.author.mention}")
#    await bot.process_commands(message)


@bot.listen('on_message')
async def listenmsg(msg):
    if msg.author == bot.user:
        return
    if msg.author.bot: return
    if 'sus' in msg.content.lower():
        channel = msg.channel
        await channel.send('https://cdn.discordapp.com/attachments/1095826652736520192/1097084226077196359/among-us-twerk.gif')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'chebin' in msg.content.lower():
        channel = msg.channel
        await channel.send('https://media.discordapp.net/attachments/1095826652736520192/1097085240108920882/WhatsApp_Image_2023-04-16_at_02.54.31.jpg?width=297&height=286')

@bot.listen('on_message')
async def listenmsg(msg):
    if 'nigg' in msg.content.lower():
        channel = msg.channel
        await channel.send('https://tenor.com/bQtER.gif')

################################################################################################################################################     

@commands.command()
async def hola(ctx):
  await ctx.reply("Hola :wave:")
bot.add_command(hola)

@commands.command()
async def mamala(ctx):
  await ctx.reply("vos hp")
bot.add_command(mamala)

@bot.command()
async def ping(ctx):
  await ctx.reply(f"Pong jaksj {round(bot.latency * 1000)}ms")

@bot.command()
async def felicitame(ctx):
    await ctx.send(f"Sos la mera bestia {ctx.author.mention} :muscle:")

@bot.command(aliases=['say', 'repetime', 'arremedame'])
async def repite(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()

@bot.command(aliases=['calculadora'])
async def calc(ctx, expression):
    symbols = ['+', '-', '*', '/', '%']
    if any(s in expression for s in symbols):
        calculated = eval(expression)
    await ctx.send(calculated)

@bot.command(aliases=['dice'])
async def dado(ctx):
    await ctx.send(str(random.randint(1, 6)))

@bot.command(aliases=['osuroll'])
async def roll(ctx, max:int=100):
    number = random.randint(1,max)
    await ctx.send(number)

def upper(argument):
    return argument.upper()
@bot.command(aliases=['grita'])
async def gritame(ctx, *, content: upper):
    await ctx.send(content)



@bot.command(aliases=['yt'])
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send('https://www.youtube.com' + search_results[0])

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return (quote)

@bot.command()
async def inspirame(ctx):
        quote = get_quote()
        await ctx.send(quote)

#def get_dogpic():
#    response = requests.get("https://dog.ceo/api/breads/image/random")
#    json_data = json.loads(response.text)
#    quote = json_data[0]['q'] + " - " + json_data[0]['a']
#    return (quote)

#@bot.command(aliases=['dog'])
#async def perro(ctx):
#    response = requests.get("")
#    image_link = response.json()["message"]
#    await ctx.send(image_link)

@bot.command(aliases=['dog', 'perro'])
async def perra(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="perra", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed) # Send the embed


#@bot.command(aliases=['sex'])
#async def sexo(ctx):
#        embed = discord.Embed(title="Sex", description="omg quiere sexo", color=discord.Color.blue())
#        embed.add_field(name="waos", value="lol", inline=False)
#        embed.add_field(name="izquierda", value="nose lol", inline=True)
#        embed.add_field(name="derecha xd", value="ojo [aqui](https://media.tenor.com/WkZleYOImDAAAAAS/its-not-something-you-cod-achieve-easily-cod.gif)", inline=True)
#        embed.set_author(name=ctx.message.author)
#        embed.set_thumbnail(url="https://culverduck.com/wp-content/uploads/2020/11/duck-animate-3-500x500.png")
#        embed.set_image(url="https://c.tenor.com/RzHjxoHF9YcAAAAd/cat-swim-in-milk-cat.gif")
#        embed.set_footer(text="Sexo")
#        embed.timestamp = datetime.datetime.now()
#        await ctx.send(embed=embed)

#def generate_response(message):
#    response = chatbot(message)[0]['generated_text']
#    return response

#@bot.command()
#async def ai(ctx, *, message):
    # Send the user's message to the ChatGPT pipeline and get the response
#    response = chatbot(message)[0]['generated_text']
    
    # Send the response to the Discord channel
#    await ctx.send(response)


@bot.command(aliases=['8ball', '8b', 'predecime', 'predict'], description='Predicción épica\n')
async def decime(ctx, *, question):
    responses = ['Simon',
             'Desde mi punto de vista, si xd',
             'Sin ningún tipo de duda, si',
             'Estoy convencidísima de que si',
             'A lo mejor',
             'Preguntale a tu mama',
             'Nel',
             'Negativo',
             'No creo',
             'Quizás xd',
             'No estoy segura',
             'Quién sabe lul',
             'Que comentario más cochón',
             'Tengo pereza de responderte eso',
             'mae algpt obvio',
             'Mamala no sé']
    await ctx.send(f'{random.choice(responses)}')

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

YTDLP_OPTIONS = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'mp3',
                'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                'restrictfilenames': True,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'ytsearch',
                'source_address': '0.0.0.0',
            }

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

@bot.command()
async def join(ctx):
    if ctx.voice_client in  bot.voice_clients:
        await ctx.reply("Ya estoy en vc")
    if ctx.author.voice is None:
        await ctx.reply("Metete a vc")
    else:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.reply("yap")

@bot.command()
async def leave(ctx):
    if ctx.author.voice is None:
        await ctx.reply("Ni estás en vc")
    else:
        if ctx.voice_client.is_connected:
            await ctx.voice_client.disconnect()
            await ctx.reply("yap")
        else:
            await ctx.reply("Ni siquiera estoy en vc, bruh")

@bot.command()
async def stop(ctx):
    if ctx.author.voice is None:
        await ctx.reply("Ni estás en vc")
    else:
        if ctx.voice_client.is_playing:
         ctx.voice_client.stop()
         await ctx.reply("ya te la paré")
        else:
         await ctx.reply("No estoy tocando nada")

@bot.command()
async def pause(ctx):
    if ctx.author.voice is None:
        await ctx.reply("Ni estás en vc")
    else:
        if ctx.voice_client.is_playing:
         ctx.voice_client.pause()
         await ctx.reply("pausado")
        else:
         await ctx.reply("No estoy tocando nada")

@bot.command()
async def resume(ctx):
    if ctx.author.voice is None:
        await ctx.reply("Ni estás en vc")
    if ctx.voice_client.is_playing:
             ctx.voice_client.resume()
             await ctx.reply("resumido")
    else:
        await ctx.reply("No estoy pausada")

def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

      
@bot.command(name='play', aliases=['p'], pass_context = True)
async def play(ctx, *, search_term:str = None):
    if ctx.author.voice is None:
        await ctx.reply("Metete a vc")        
    if ctx.author.voice:
        voice = None
    if search_term == None:
        await ctx.send('No hay canción especificada.')
        return
    if not ctx.voice_client:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
    else:
            if search_term[0:4] == "http" or search_term[0:3] == "www":
                with yt_dlp.YoutubeDL(YTDLP_OPTIONS) as ydl:
                    info = ydl.extract_info(search_term, download = False)
                    title = info["title"]
                    url = search_term
 
            if search_term[0:4] != "http" and search_term[0:3] != "www":
                with yt_dlp.YoutubeDL(YTDLP_OPTIONS) as ydl:
                    info = ydl.extract_info(f"ytsearch:{search_term}", download = False)["entries"][0]
                    title = info["title"]
                    url = info["webpage_url"]
                    voice = ctx.guild.voice_client
            if voice.is_playing():
#                queue.append(title)
                await ctx.send(f"**Agregada a la lista:** {title}")
            else:
                voice.play(discord.FFmpegPCMAudio(f"{title}.mp3")) #after = lambda e : check_queue())
                await ctx.send(f"**Sonando** {title}")
            
       #url = YT.singleSearch(search_term)

            with yt_dlp.YoutubeDL(YTDLP_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                playUrl = info['url']

            source = FFmpegPCMAudio(source=playUrl, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",options="-vn")
            voice.play(source)

##########################################################################
########################################################################################

bot.run("NzQwNjgxNTU3NzMxMzExNjI3.Guix_l.Ib-A1MRhmtme4Iz9YqrcixPAHhS_ZbuW10dySc")
