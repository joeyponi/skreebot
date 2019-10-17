# SkreeBot
A bat pony bot that does bat pony things

## Features
- Skrees a lot
- Reacts with bat emojis
- Can search for bat pony pics using the !bat command

## Dependencies
- Python 3
- Requests
- Discord.py

## Installation
Install the dependencies

    $ pip install requests
    $ pip install discord.py

Move/copy config.json.example to config.json, then add your Discord App's token and Derpibooru API key (for filtering purposes)

If testing, change "runmode" to "test" in config.json, this will allow you to use the !stop command to (usually) shutdown the bot quickly

Run the bot

    $ python skreebot.py