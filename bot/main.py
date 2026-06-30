import discord
from discord.ext import commands
from bot.config import DISCORD_TOKEN
from bot.rick_ai import RickAI

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
rick_ai = RickAI()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Wubba Lubba Dub-Dub! The bot is online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Interdimensional Cable"))

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands first
    await bot.process_commands(message)

    # Check if bot is mentioned, replied to, or if the message contains "rick"
    is_reply = message.reference is not None and getattr(message.reference.resolved, 'author', None) == bot.user
    
    if bot.user in message.mentions or is_reply or "rick" in message.content.lower():
        # Clean the message content
        clean_content = message.clean_content.replace(f"@{bot.user.name}", "").strip()
        if clean_content.lower().startswith("rick,"):
            clean_content = clean_content[5:].strip()
        elif clean_content.lower().startswith("rick"):
            clean_content = clean_content[4:].strip()
            
        async with message.channel.typing():
            response = await rick_ai.generate_response(message.channel.id, clean_content)
        
        # Split response if it's too long for Discord (limit is 2000 chars)
        if len(response) > 2000:
            for i in range(0, len(response), 2000):
                await message.reply(response[i:i+2000])
        else:
            await message.reply(response)

@bot.command(name='reset')
async def reset_memory(ctx):
    """Clears Rick's memory of the current channel."""
    rick_ai.reset_memory(ctx.channel.id)
    await ctx.send("*burp* I wiped my memory of this channel. Who the hell are you people again?")

def run():
    if not DISCORD_TOKEN:
        print("Error: DISCORD_TOKEN is missing. Please check your .env file.")
        return
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    run()
