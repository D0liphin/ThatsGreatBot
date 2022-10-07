import discord, dotenv, os
dotenv.load_dotenv()

client = discord.Client(intents=discord.Intents(274945084480))

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("received", message)
    await message.channel.send("ping")

client.run(os.environ.get("TOKEN"))

