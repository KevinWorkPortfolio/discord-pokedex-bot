# Discord Pokédex Bot

A simple Discord bot built with Python that allows users to search for Pokémon information using commands.

## Project Features

- `!pokedex <name>` → Shows information about a Pokémon  
- Suggests similar names if the input is incorrect  
- `!list` → Displays available Pokémon  
- `!help` → Shows available commands  
- Uses Discord embeds for better message formatting  

## Tech Stack

- Python  
- discord.py  
- python-dotenv  

## Installation Guide

1. Clone the repository:

2. Install dependencies:
pip install -r requirements.txt

3. Create a `.env` file and add your Discord token:
DISCORD_TOKEN=your_token_here in bot.py file

4. Run the bot:
python bot.py

## Notes

- The Discord token is not included for security reasons  
