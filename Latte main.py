import discord
from discord.ext import commands
import random
import datetime
from urllib import parse, request
import re
import requests, json
import os
import music

cogs = [music]

#intents = discord.Intents.default()
#intents.message_content = True

bot = commands.Bot(command_prefix=["lat ", "Lat "], intents=discord.Intents.all(),
activity=discord.Game(name="Soy hija de KevinRJF"))

for i in range(len(cogs)):
    cogs[i].setup(bot)

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

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Qué? {ctx.author.mention} no te entendí xd \n\n(In english: {(error)})") 

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
async def latteonmsg(msg):
    if 'latte' in msg.content.lower():
        channel = msg.channel
        await channel.send('yo cuando')

################################################################################################################################################     

@bot.command()
async def hola(ctx):
  await ctx.reply("Hola :wave:")

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

@bot.command(aliases=['sex'])
async def sexo(ctx):
        embed = discord.Embed(title="Sex", description="omg quiere sexo", color=discord.Color.blue())
        embed.add_field(name="waos", value="lol", inline=False)
        embed.add_field(name="izquierda", value="nose lol", inline=True)
        embed.add_field(name="derecha xd", value="ojo [aqui](https://media.tenor.com/WkZleYOImDAAAAAS/its-not-something-you-cod-achieve-easily-cod.gif)", inline=True)
        embed.set_author(name=ctx.message.author)
        embed.set_thumbnail(url="https://culverduck.com/wp-content/uploads/2020/11/duck-animate-3-500x500.png")
        embed.set_image(url="https://c.tenor.com/RzHjxoHF9YcAAAAd/cat-swim-in-milk-cat.gif")
        embed.set_footer(text="Sexo")
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

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

bot.run("NzQwNjgxNTU3NzMxMzExNjI3.Guix_l.Ib-A1MRhmtme4Iz9YqrcixPAHhS_ZbuW10dySc")