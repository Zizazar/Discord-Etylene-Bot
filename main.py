import discord
import json
from random import randint, choice 
with open('phrases.json') as f:
    phrases = json.load(f)

etylen = 0
bot = discord.Bot(command_prefix="!",
                   intents=discord.Intents.all(),
                   status=discord.Status.online
                   )

@bot.slash_command(name="etylen",str=None)
async def hello(ctx):
    name = ctx.author.name
    await ctx.respond(f"{etylen}<:minus_servak:1200151110971826187>")

@bot.listen('on_message')
async def on_message(message):
        if message.author == bot.user:
            return
        for section, commands in phrases.items():
            if section in message.content.lower():
                if section == "етилен": 
                    global etylen
                    etylen += 1
                    await message.add_reaction("<:minus_servak:1200151110971826187>")
                if randint(1, 6) == 1:
                        await message.channel.send(choice(commands))
                    

bot.run('')
