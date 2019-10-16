# Import libraries
import discord
import json

# Load config
config = json.load(open('config.json'))

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
        await message.channel.send('eeeeeeeeee!')

# Run the bot
bot.run(config['token'])