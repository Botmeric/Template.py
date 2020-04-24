## Template.py
A basic Python template for a Discord Bot

## Running

1. **Install Python v3.6 or higher**

    This is required to actually run the bot.

2. **Install dependencies**

    - `cd` to the working directory of your clone of this repository
    - Execute: `pip3 install -U -r requirements.txt`

3. **Create an Application with Discord**

    Create an application on Discord's website https://discordapp.com/developers/applications

4. **Setup configuration**

    Edit the configuration of `/config/config.dev.json`

    ```py
    owner_ids = [] # a list of Discord user IDs who own the bot
    id = '' # your bot's client ID
    token = '' # your bot's token
    ```

## Documentation

- Discord's API: https://discordapp.com/developers/docs/intro
- Discord.py https://discordpy.readthedocs.io/en/latest/

## Requirements

- Python v3.6+
- discord.py v1.3.0+
