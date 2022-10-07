import discord, dotenv, os
dotenv.load_dotenv()

intents = discord.Intents(8);
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.channel.send("ping")

client.run(os.environ.get("TOKEN"))

