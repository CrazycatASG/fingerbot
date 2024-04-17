import os, discord
from dotenv import load_dotenv

def guessingnum():
    pass

async def russianroulette(player):
    guild = client.get_guild(os.environ.get("GUILD_ID"))
    for member in guild.members: 
        if member.name == player:
            pass
        else:
            await message.channel.send("{player} is not a member of the server.")


load_dotenv()