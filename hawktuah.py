import discord

TOKEN = "a51dc72509873b7a36250357de015998f5b503214eb3f83fc36a910afb798917"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

VALID_PREFIXES = {
    "hawk", "honk", "sock", "talk", "walk", "rock", "knock",
    "clock", "mock", "shock", "dock", "block", "stock", "talk"
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.lower().split()
    if len(words) >= 2 and words[-1] == "tuah" and words[-2] in VALID_PREFIXES:
        response = f"{message.author.mention} {words[-2].upper()} TUAH!"
        await message.channel.send(response)

client.run(TOKEN)
