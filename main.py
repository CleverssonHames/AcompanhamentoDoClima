
import discord  
from discord.ext import tasks
from atualizaClima import Atualizaclima
import asyncio 


client = discord.Client(intents=discord.Intents.default())


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'Você esta logado com {client.user}')

@client.event
async def on_message(message):

  global on_clima

  if message.author == client.user:
    return
  
  if message.content.startswith('comandos'):
    msg = (
    '\n** #COMANDOS **'
    '\n👉 Ver clima: +Nome da cidade'
    '\n👉 Parar: -p'
    )
    await message.channel.send(msg)
  
  if message.content.startswith('+'):
    cidade = message.content.split("+", 2)
    
    
    @tasks.loop(minutes=60)
    async def on_clima():
      tempo = Atualizaclima.atu_clima(cidade[1])
      await message.channel.send(tempo)
    on_clima.start()

  if message.content.startswith('-p'):
    msg = ("Que pena!"
          "\nQuando precisar é só chamar." 
          "\nAté mais! 👋")
    await message.channel.send(msg)      
    on_clima.cancel()

client.run(
  'MTA4OTU4NjA2MTUwOTkzNTE5NQ.GTC780.qxidaBe0SaEuxuXO7Hd64QihLSv_367kPc4gZY')
