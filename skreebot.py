# Import libraries
import discord
import json
import random
from derpibooru import Search, sort

# Load config
config = json.load(open('config.json'))

# Bat pony noises
bat_noises = [
    'eeeeeeeeee!',
    'Skree!',
    'Skreeeeeee!'
]

# Create the bot instance
bot = discord.Client()

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

# Run the bot
bot.run(config['token'])