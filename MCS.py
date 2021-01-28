from discord.ext.commands.core import command
import discord
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()
token = 'ODA0MzU3NTEyMzI0NTc5MzI5.YBLKTw.sVjlMRHHCtISNJAHEp--5ZDLTxw'

@commands.cooldown(1, 900, commands.BucketType.user)


# boops the mentioned user
@bot.command(name='boop')
async def boop(ctx):
    user = ctx.message.mentions
    userid = user[0].id
    boops = ['*boop*', '**boop**', 'bOoP', '~~boop~~', 'BOOOOOOOP', 'boop?', 'boop.', 'MEGA BOOP', '**ULTRA BOOP!!!!**']
    boop = random.choice(boops)
    theboop = str(boop) + " <@!" + str(userid) + ">"
    await ctx.send(theboop)
    await ctx.message.delete()

# audrey is not cool
@bot.command(name='audrey_is_cool')
async def audrey(ctx):
    await ctx.send("You lie.")

# returns the latency of the bot
@bot.command(name='ping')
async def ping(ctx):
    ping = bot.latency
    await ctx.send(ping)

@boop.error
async def bot_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        errorMessage = 'Please refrain yourself <@!' + str(ctx.author.id) + '>, try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(errorMessage)
        await ctx.message.delete()
    else:
        raise error


bot.run(token)