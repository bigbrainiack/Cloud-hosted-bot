import discord
import random
import aiohttp
import asyncio
import youtube_dl
import os
from discord.utils import get
from async_timeout import timeout
from discord.ext import commands

TOKEN = 'ZVG5xuJZVDq9-MtTFKwj1ItLGjZWmLB2'

client =commands.Bot(command_prefix = '.')

#Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='askiitians.com | .commands'))
    print('Bot is ready.')

#Command
@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title = 'Commands',
        colour = discord.Colour.orange()
    )

    embed.set_footer(text = 'askiitians.com')
    embed.set_author(name = 'askIITians'),
    embed.add_field(name = 'Talk', value = '``hi`` ``gm``', inline = False)
    embed.add_field(name = 'Fun', value = '``8ball`` ``ping``', inline = False)
    embed.add_field(name = 'askIITians Course Manual', value = ' ``room`` ``tta1`` ``tta2`` ``holiday``', inline = False)
    embed.add_field(name = 'Books', value = ' ``room`` ``module``', inline = False)
    await ctx.send(embed=embed) 

#Timetable A1
@client.command()
async def tta1(ctx):
    embed = discord.Embed(
        title = 'Time Table for Chandra A1',
        colour = discord.Colour.orange()
    )

    embed.set_footer(text = 'askiitians.com')
    embed.set_author(name = 'askIITians'),
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/752088825487949834/752089714269487185/unknown.png' )
    await ctx.send(embed=embed)

#Timetable A2
@client.command()
async def tta2(ctx):
    embed = discord.Embed(
        title = 'Time Table for Chandra A2',
        colour = discord.Colour.orange()
    )

    embed.set_footer(text = 'askiitians.com')
    embed.set_author(name = 'askIITians'),
    embed.set_image(url = 'https://media.discordapp.net/attachments/752088825487949834/752406201655885894/unknown.png?width=850&height=188' )
    await ctx.send(embed=embed)

@client.command()
async def gm(ctx):
    await ctx.send(f'Good Morning!')

#Hi command
@client.command()
async def hi(ctx):
    await ctx.send(f'Hello There.')


#Askiit classroom
@client.command()
async def room(ctx):
    await ctx.send(f'Here are your upcoming classes https://www.askiitians.com/my-classroom.aspx')

#Modules
@client.command()
async def module(ctx):
    await ctx.send(f'Here are the modules https://drive.google.com/open?id=1TGWLZ_vuPpy7TPxUkErna5j5S8aJxfth')
 #8ball command
@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *,question):
    responses = ['It is certain.',
                 'It is decidedly so.'
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(random.choice(responses))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')

#Holidays 
@client.command()
async def holiday(ctx):
    embed = discord.Embed(
        title = 'Holiday List',
        colour = discord.Colour.orange()
    )

    embed.set_footer(text = 'askiitians.com')
    embed.set_author(name = 'askIITians'),
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/752088825487949834/752092526588198993/unknown.png' )
    await ctx.send(embed=embed)

@client.command()
async def news(ctx):
     async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/news/.json') as r:
            res = await r.json()
            embed = discord.Embed(
                title= 'NEWS',
                color=discord.Color.blue()
            )
            embed.add_field(name=res['data'] ['children'] [random.randint(0, 25)] ['data'] ['title'], value= '-', inline=False)
            await ctx.send(embed=embed)



client.run(TOKEN)