# Import libraries
import discord
import json
import random
import urllib
from discord.ext import commands
from discord.ext.commands import CommandNotFound

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
@bot.command(pass_context=True)
async def bat(ctx,*,user_search_string=''):
    # Define base search string
    search_string = 'bat pony,'

    # Add ratings to search string
    if (ctx.channel.is_nsfw()) and ("safe" not in user_search_string.lower()):
        search_string += '(explicit || questionable || suggestive)'
    else:
        search_string += 'safe'

    # Add user search
    if(len(user_search_string) > 0):
        search_string += ',' + user_search_string

    # Generate random seed for search
    random_seed = str(random.randint(100000,999999))

    # Generate the search url
    search_url = 'https://derpibooru.org/search.json?key=' + config['derpikey'] + '&perpage=1&sf=random:' + random_seed + '&q=' + urllib.parse.quote(search_string)

    # Get result
    search_response = urllib.request.urlopen(search_url).read()
    search_data = json.loads(search_response)

    # Output result (or fail if no result)
    try:
        search_result = "https://derpibooru.org/" + str(search_data['search'][0]['id'])
        await ctx.send(search_result)
    except IndexError:
        await ctx.send("No result found. Sad skree :(")

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

# Ignore commands from other bots (don't show error)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

# Stop command
if(config['runmode'] == 'test'):
    @bot.command()
    async def stop(ctx):
        exit()

# Run the bot
bot.run(config['token'])