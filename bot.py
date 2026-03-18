import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Carga los chistes desde archivo
def cargar_chistes():
    with open("chistes.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

chistes = cargar_chistes()

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")
    print(f"{len(chistes)} chistes cargados")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Responde si hay mención
    if message.mentions:
        chiste = random.choice(chistes)
        await message.channel.send(chiste)

bot.run(os.getenv("DISCORD_TOKEN"))
