import os
import random
from tinydb import TinyDB, Query
from discord.ext import commands
from dotenv import load_dotenv
import discord
load_dotenv() #!add 2021-11-0 "Hello world"="A test input"
TOKEN = os.getenv('DISCORD_TOKEN')
client=discord.Client()
db=TinyDB('db.json')
bot = commands.Bot(command_prefix='!')

@bot.command(name='add')
async def _command(ctx,*args):
        #!add {date} {time} {event} {description}
        #db.insert({'user':ctx.author.id})
        response = ""

        db.insert({'user':ctx.author.id,'date':args[0],'time':args[1],'event':args[2],'desc':args[3]})

        await ctx.channel.send("Event:"+args[2]+" created")

bot.run(TOKEN)
