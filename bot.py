import os
import discord 
import difflib
from discord.ext import commands   
from pokedex_data import pokemon_info
from dotenv import load_dotenv

load_dotenv()

# Definisci gli intents e crea il bot
intents = discord.Intents.default()
intents.members = True  # se vuoi i membri
intents.messages = True # per ricevere eventi messaggi (ma non il contenuto testuale)


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} è online!')

@bot.command()
async def pokedex(ctx, *, name: str):
    nome = name.lower()

    if nome in pokemon_info:
        data = pokemon_info[nome]

        sprite_url = data.get('sprite_pixel_art') or "https://example.com/fallback_image.png"
        description = data.get('descrizione', 'Descrizione non disponibile.')
        color = data.get('colore', 0x000000)

        embed = discord.Embed(
            title=f"{nome.capitalize()}",
            description=description,
            color=color
        )
        embed.set_image(url=sprite_url)

        try:
            await ctx.send(embed=embed)
        except Exception as e:
            print(f"Errore invio embed: {e}")

    else:
        suggerimenti = difflib.get_close_matches(nome, pokemon_info.keys(), n=3)

        if suggerimenti:
            await ctx.send(f"❌ Pokémon non trovato. Intendevi: {', '.join(suggerimenti)}?")
        else:
            await ctx.send("❌ Pokémon non trovato.")

@bot.command()
async def list(ctx):
    pokemon_names = list(pokemon_info.keys())

    embed = discord.Embed(
        title="📖 Lista Pokémon",
        description=", ".join(pokemon_names[:50]),  # primi 50 per non esagerare
        color=0x00ff00
    )

    embed.set_footer(text="Usa !pokedex <nome> per vedere i dettagli")

    await ctx.send(embed=embed)

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="📖 Comandi disponibili",
        color=0x3498db
    )

    embed.add_field(name="!pokedex <nome>", value="Mostra info del Pokémon", inline=False)
    embed.add_field(name="!list", value="Mostra lista Pokémon disponibili", inline=False)
    embed.add_field(name="!help", value="Mostra questo messaggio", inline=False)

    await ctx.send(embed=embed)

# Avvia il bot usando la variabile d'ambiente
bot_token = os.getenv("DISCORD_TOKEN")
if not bot_token:
    raise ValueError("Token Discord non trovato. Assicurati che DISCORD_TOKEN sia impostato nel file .env.")

bot.run(bot_token)