# Finger, the official bot for The Gathering under The Stars, The Royal Army of the Kingdom of Samuel, amongst others.
# This software is licensed under the MIT license, which can be found included in the source code or at https://mit-license.org

import discord, os, random, logging, games, asyncio
from dotenv import load_dotenv

topics = []

with open("questions.txt") as questions:
    lines = questions.readlines()
    topics = [line.strip() for line in lines]

class finger(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {client.user}')

    async def on_message(self, message):
        if message.author == client.user: return
        if message.content.startswith('.topic'): await message.channel.send(topics[random.randint(0, 35)])
        if message.content.startswith('.russianroulette') or message.content.startswith(".rr"):
            try:
                asyncio.run(games.russianroulette())
            except TypeError:
                await message.channel.send("You're missing the player you want to play with.")
        if message.content.startswith('.muhammed'): await message.channel.send("the voices get louder every day <:imlosingit:1193204105917759548>")
intents = discord.Intents.default()
intents.message_content = True

client = finger(intents=intents)

load_dotenv()
client.run(os.environ.get("TOKEN"))
#