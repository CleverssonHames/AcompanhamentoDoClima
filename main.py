
import discord  
from discord.ext import commands, tasks
from atualizaClima import Atualizaclima
import asyncio 

#client = discord.Client(intents=intents)
#client = discord.Client(intents=discord.Intents.default())


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
  print(f'Você esta logado com {bot.user}')



@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  global on_clima
  
  if '&' in message.content:
    cidade = message.content.split("&", 2)

    @tasks.loop(minutes=60)
    async def on_clima():
      tempo = Atualizaclima.atu_clima(cidade[1])
      await message.channel.send(tempo)
    on_clima.start()

  if 'stop' in message.content:
    msg = ("Que pena!"
        "\nQuando precisar é só chamar." 
        "\nAté mais! 👋")
    await message.channel.send(msg)      
    on_clima.cancel()

  await bot.process_commands(message)



@bot.command(name='Ola')
async def ola(ctx):
  await ctx.message.channel.send('Olá querids')



@bot.command(name='comandos')
async def comandos(ctx):
  msg = (
    '\n** #COMANDOS **'
    '\n👉 Ver clima: +Nome da cidade'
    '\n👉 Parar: -p'
    )
  await ctx.message.channel.send(msg)

bot.run(${{ TOKEN }})
