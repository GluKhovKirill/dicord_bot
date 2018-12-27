import discord
from discord.ext import commands
import sys


owner = "Kirill"
TOKEN = 'NTI3ODMzNjMxMjM5MTc2MTk2.DwZlkQ.1i3psy23Ot75lh4maHE2C2ZWDpk'
prefix = '$'
prior_channel = "main"
greeting = "Всем привет! :wave:"

client = commands.Bot(command_prefix=prefix, command_not_found="Я не знаю такой команды (\""+prefix+"{}\")")

def check_acces(roles, name=False):
    for role in roles:
        if role.name == name or role.permissions.administrator:
                return True
    return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for channel in client.get_all_channels():
        #print(channel.name, dir(channel))
        if channel.name == prior_channel:
            await channel.send(greeting)
    


@client.event
async def on_message(message):
    channel = message.channel
    author = message.author.name
    author_id = author #ПЕРЕДЕЛАТЬ
    is_bot = message.author.bot
    msg = message.content
    
    #print("CHNL:", message.channel)
    print("MSG:",message)
    
    if not is_bot:
        if msg.strip()[0] == prefix:
                print("CMD")
                await client.process_commands(message)

            
    
@client.command()
async def die(ctx):
    global d
    d=ctx
    author = ctx.author
    if check_acces(author.roles, name="moderator"):
        await ctx.send('Пока! :wave:')
        print("BYE")
        sys.exit(True)    
    else:
        await ctx.send('{}, ты ничего не перепутал?'.format(author.name))

'''
@client.command_not_found()
async def not_command():
    print("ERR:")
    await message.channel.send('{}, я не понял, что ты хочешь... ("{}")'.format(author, msg))
'''
client.run(TOKEN)
