import discord
from openai import OpenAI
import os

# Usa variable de entorno (más seguro)
client_ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Detecta menciones
    if message.mentions:
        usuario = message.mentions[0].name

        try:
            respuesta = client_ai.responses.create(
                model="gpt-4.1-mini",
                input=f"Haz un chiste de humor negro corto sobre {usuario}, en español, estilo sarcástico pero gracioso"
            )

            await message.channel.send(respuesta.output_text)

        except Exception as e:
            print(e)
            await message.channel.send("Error generando respuesta 😢")

# TOKEN de Discord (NO lo subas a GitHub)
bot.run(os.getenv("DISCORD_TOKEN"))
