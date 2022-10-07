from random import randint
import discord, dotenv, os
from responses import *
dotenv.load_dotenv()

BOT_ID = 1027963972164518039
client = discord.Client(intents=discord.Intents(
    messages=True, 
    message_content=True
))



@client.event
async def on_ready():
    print(f"bot ready {client}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for mention in message.mentions:
        if mention.id == BOT_ID:
            await message.channel.send(POSITIVE_RESPONSES[randint(0, len(POSITIVE_RESPONSES))])
            break;
    

client.run(os.environ.get("TOKEN"))

