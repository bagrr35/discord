import discord
from discord.ext import commands
from config import token
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')

@client.command()
async def nasılsın(ctx):
    await ctx.send('İyiyim, sen nasılsın?')

@client.command()
async def Merhaba(ctx):
    await ctx.send('Merhaba, nasıl yardımcı olabilirim?')

@client.command()
async def yazıtura(ctx):
    await ctx.send("1'mi 2'mi?")

@client.command()
async def bir(ctx):
    await ctx.send("Yazı!")

@client.command()
async def iki(ctx):
    await ctx.send("Tura!")

@client.command()
async def info(ctx):
    await ctx.send("Ben, python diliyle yapıldım!")
    
client.run(token)