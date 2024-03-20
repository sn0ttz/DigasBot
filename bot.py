from discord.ext import commands
import discord
import random
import tokens


TOKEN = tokens.tokens.BOT_TOKEN
CHANEL_ID = tokens.tokens.CHANNEL_TOKEN

bot = commands.Bot(command_prefix='d!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Olá, {bot.user}')
    channel = bot.get_channel(CHANEL_ID)
    await channel.send('Online and ready to go!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def douche(ctx, member: discord.Member = None):
    await ctx.send('@ Someone you douche!' if member is None else f'{member.mention} is a douche!')

@bot.command()
async def add(ctx, a, b):
    try:
        a = int(a)
        b = int(b)
        ans = a+b
    except Exception as e:
        ans = 'Please insert two valid numbers!'

    await ctx.send(ans)

@bot.command()
async def helpme(ctx):
    await ctx.send('PREFIX: d!\nCOMMANDS:\n d!douche @someone \n d!ping \n d!add num1 num2 \n d!helpme \n d!rdice maximum')

@bot.command()
async def rdice(ctx, a):
    try:
        a = int(a)
        if a <= 1:
            x = 'Please insert a number greater than 1!'
        else:
            x = random.randint(1,a)
    except Exception as e:
        x = 'Please insert a valid number!'
    await ctx.send(x)

bot.run(TOKEN)