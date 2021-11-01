import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='timetable')
async def _command(ctx):
   

    response = "Can you enter the times(in UTC) in your timetable seperated with commas? For example:\n`09:00,09:40,10:20`\n"
    await ctx.send(response)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["y", "n"]
    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() == "y":
        await ctx.send("You said yes!")
    else:
        await ctx.send("You said no!")

bot.run(TOKEN)
