import discord
import json
import youtube_dl
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = 'b!')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='212 Servers.', type = 2))
    await asyncio.sleep(5)
    await client.change_presence(game=discord.Game(name='So much Coding.'))
    await asyncio.sleep(5)
    print('Ready, Freddy.')

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open ('users.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open ('users.json', 'w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
    if ('cock') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('penis') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('vagina') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('motherfucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('tits') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucking') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('anal') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('porn') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('pussy') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if message.content == 'b!ping':
        await client.send_message(message.channel,'Pong!')
    if message.content == 'b!version':
        await client.send_message(message.channel,'Current Version: **Jarvis 2.3**')
    if message.content == 'b!credits':
        await client.send_message(message.channel,'**Credits to WolfHussain for creating me with such IQ and thinking ability. Thank him please :)**')
    if message.content == 'b!servercount':
        await client.send_message(message.channel,'*Currently working for approximatly 212 Servers*')
    await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('*Messages Deleted, Sir.*')

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await client.say(":boot: Cya, {}.".format(user.name))
    await client.ban(user)
    print (".ban on {}".format(user.name))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await client.say(":boot: Cya, {}.".format(user.name))
    await client.kick(user)
    print (".kick on {}".format(user.name))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *, arg = None):
    if arg is None:
        await client.say("Please provide a reason for {}'s warning.".format(user.name))
        return False
    reason = arg
    author = ctx.message.author
    server = ctx.message.server
    embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
    embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
    embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
    await client.say(embed=embed)
    await client.send_message(user, "You have been warned for: {}".format(reason))
    await client.send_message(user, "from: {} server".format(server))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def mute(ctx, user: discord.Member, *, arg):
    if arg is None:
        await client.say("please say a reason to {}".format(user.name))
        return False
    reason = arg
    author = ctx.message.author
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.add_roles(user, role)
    embed = discord.Embed(title="Mute", description=" ", color=0xFFA500)
    embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
    embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info():
    embed = discord.Embed(
        title = 'Name:',
        description = 'Jarvis#3765',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Information Section:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Creator:', value='Yo#0953.', inline=False)
    embed.add_field(name='Creation Date:', value='12th Dec 2018.', inline=False)
    embed.add_field(name='Coded from:', value='3.6.5 Python Shell.', inline=False)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    await client.say('Help is on its way! Check your DM.')
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name='Help | Commands')
    embed.add_field(name='b!info', value='Gives you information about me.', inline=False)
    embed.add_field(name='b!clear', value='Delete the number of messages you want.', inline=False)
    embed.add_field(name='b!ban', value='Bans a player.', inline=False)
    embed.add_field(name='b!kick', value='Kicks a player.', inline=False)
    embed.add_field(name='b!version', value='Gives you the bots version.', inline=False)
    embed.add_field(name='b!credits', value='Gives you the credits to who made me.', inline=False)
    embed.add_field(name='b!servercount', value='Gives you the number of servers i am working on.', inline=False)

    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def playerinfo(ctx, user: discord.Member):
    embed = discord.Embed(title='{} Info:'.format(user.name), description='Here is  what i could find, Sir.', color=0x00ff00)
    embed.add_field(name='Name:', value='user.name', inline=False)
    embed.add_field(name='ID:', value='user.id', inline=False)
    embed.add_field(name='Status:', value='user.status', inline=False)
    embed.add_field(name='Highest Role:', value='user.top_role', inline=False)
    embed.add_field(name='Joined At:', value='user.joined_at', inline=False)
    embed.add_thumbnail(url='user.avatar_url')

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(
        title = 'Server Information:',
        description = 'Information is on its way!',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Server Information:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Server Name:', value='Custom Discord Bot Testing Server.', inline=False)
    embed.add_field(name='Creation Date:', value='4th Dec 2018.', inline=False)
    embed.add_field(name='Made By:', value='Discord | Discord, Please Sponser Me.', inline=False)
    embed.add_field(name='ID:', value='ctx.message.server.id', inline=False)
    embed.add_field(name='Roles:', value='len(ctx.message.server.roles)', inline=False)
    embed.add_field(name='Members:', value='len(ctx.message.server.members)', inline=False)

    await client.say(embed=embed)

client.run('NTMwODM2MTUyOTcwOTAzNTc0.DxFLfw.cUwmW3JLLKCvS_5vuHVEWqlUKb0')
