# Import libraries
import discord
import json
import random
from derpibooru import Search, sort
from discord.ext import commands

# Load config
config = json.load(open('config.json'))

# Bat pony noises
bat_noises = [
    'eeeeeeeeee!',
    'Skree!',
    'Skreeeeeee!'
]

# Create the bot instance
bot = commands.Bot(command_prefix='!')

# Respond to messages that contain skrees
@bot.event
async def on_message(message):
    # Prevent bot from triggering itself
    if message.author == bot.user:
        return

    # Respond to skrees
    if "skree" in message.content.lower():
        emoji = '\N{Bat}'
        await message.add_reaction(emoji)

    # Respond to long skree
    if "skreeee" in message.content.lower():
        await message.channel.send(random.choice(bat_noises))

    # Process commands
    await bot.process_commands(message)

# Search for a bat
@bot.command()
async def bat(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send('lewd bat!')
    else:
        await ctx.send('bat!')

# Bot info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='SkreeBot', description='A bat pony bot that does bat pony things.', color=0x7a3c8c)
    embed.add_field(name='Author', value='Joey')
    embed.add_field(name='Server Count', value=f'{len(bot.guilds)}')
    await ctx.send(embed=embed)

# Bot help
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='SkreeBot', description='A bat pony bot that does bat pony things.\n\u200b', color=0x7a3c8c)
    embed.add_field(name='!bat', value='Searches for bat ponies on Derpibooru. Specify tags to refine your search.', inline=False)
    embed.add_field(name='!info', value='Shows some info about the bot.', inline=False)
    embed.add_field(name='!help', value='Shows this help dialog.', inline=False)
    embed.add_field(name='Bat Noises', value='This bot likes bat noises. Making them may entice a reaction.', inline=False)
    await ctx.send(embed=embed)

# Run the bot
bot.run(config['token'])