import discord
from discord.ext import commands
from bot_token import token
from detect_class import detect_bird

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    
    if ctx.message.attachments:
        await ctx.send("Algılama başladı")
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"img/{file_name}"
            await attachment.save(file_path)
            await ctx.send("Resim kaydedildi")
            name, score = detect_bird("converted_keras/keras_model.h5","converted_keras/labels.txt",file_path)
            #name, score = ("güvercin",99)
            await ctx.send(f"Bu bir {name.strip()}, bundan %{int(score*100)} eminim.")
            # if name == "sparrow":
            #     await ctx.send("")
    else:
        await ctx.send("Lütfen komutla beraber bir resim yükleyin.")


bot.run(token)
