import discord
import os
from openai import OpenAI

# Cliente de IA
client_ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Intents necesarios
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
        usuario = message.mentions[0].display_name

        try:
            respuesta = client_ai.responses.create(
                model="gpt-4.1-mini",
                input=f"Haz un chiste de humor negro corto sobre {usuario}, en español, tono sarcástico pero gracioso"
            )

            # EXTRAER TEXTO (compatible con sk-proj)
            texto = ""
            for item in respuesta.output:
                if item.type == "message":
                    for content in item.content:
                        if content.type == "output_text":
                            texto += content.text

            await message.channel.send(texto if texto else "No se pudo generar 😢")

        except Exception as e:
            print("ERROR:", e)
            await message.channel.send(f"Error: {e}")

# Ejecutar bot
bot.run(os.getenv("DISCORD_TOKEN"))
