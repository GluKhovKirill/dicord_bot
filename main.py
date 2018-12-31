import discord
from discord.ext import commands
import sys


owner = "Kirill#8322"
operators = [owner, "Andrew 45743#5197"]
TOKEN = 'NTI3ODMzNjMxMjM5MTc2MTk2.DwZlkQ.1i3psy23Ot75lh4maHE2C2ZWDpk'
prefix = '!'
prior_channel = "main"
greeting = "Всем привет! :wave: \n (P.S. Префикс для команд: \"{}\")".format(prefix)
log_output = "output.txt"

client = commands.Bot(command_prefix=prefix, command_not_found="Я не знаю такой команды (\""+prefix+"{}\")")

def check_acces(author, name=False):
    is_owner = "#".join([author.name, author.discriminator])
    if is_owner in operators:
        return True
    roles = author.roles
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
    with open(log_output, "a") as log:
        log.write("*"*10+"\nSTARTED\n")
    


@client.event
async def on_message(message):
    print(message.author)
    channel = message.channel
    sender = "#".join([message.author.name, message.author.discriminator])
    is_bot = message.author.bot
    msg = message.content
    with open(log_output, "a") as log:
        data = ["CHANNEL: "+str(channel), "SENDER: "+sender, "MSG: "+str(msg), "IsBot: ", str(is_bot)]
        log.write("|".join(data)+"\n")
    
    #print("CHNL:", message.channel)
    print("MSG:",message)
    
    if not is_bot:
        global m
        m = message
        if msg.strip()[0] == prefix:
                print("CMD")
                await client.process_commands(message)
            
    
@client.command(brief='Отключение бота', description='Отключение бота (только для владельца и ограниченного круга доверенных лиц)')
async def die(ctx):
    global d
    d=ctx
    author = ctx.author
    print("EMM")
    if check_acces(author, name="moderator"):
        await ctx.send('Пока! :wave:')
        print("BYE")
        sys.exit(True)    
    else:
        await ctx.send('{}, ты ничего не перепутал?'.format(author.name))

@client.command(brief=prefix+'hi [msg]', description='Отправка вашего сообщения от имени бота')
async def hi(ctx, msg=None, *other):
    if not msg:
        msg = "И что я должен тебе сказать? И зачем?.."
    else:
        if other:
            msg = msg + " " + " ".join(other)
    await ctx.send("BOT: {}".format(msg))

'''
@client.command_not_found()
async def not_command():
    print("ERR:")
    await message.channel.send('{}, я не понял, что ты хочешь... ("{}")'.format(author, msg))
'''
client.run(TOKEN)
