import random
import datetime
import discord
from discord.ext import commands
from discord.ext import tasks
import feedparser
from local import TOKEN

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@tasks.loop(minutes=30)
async def blogger(ctx):
    channel = bot.channel(634876030548574228)
    currentTime = datetime.datetime.utcnow
    minusThirty = datetime.time(hour = currentTime.hour, minute = currentTime.minute-30, second = 0)
    blog = feedparser.parse('https://blog.flat.io/rss/')
    if(currentTime.minute == 0 | currentTime.minute == 30):
        postTime = blog.entries[0].published_parsed
        postingTime = datetime.time(hour = postTime[3], minute = postTime[4], second = postTime[5])
        if(postingTime <= currentTime & postingTime > minusThirty):
            message = blog.entries[0].link
            await channel.send(message)

        

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


bot.run(TOKEN)