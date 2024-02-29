import os
from discord.ext import commands
import discord

# Define intents
intents = discord.Intents.default()
intents.members = True

# Create a new bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='/', intents=intents)

# Event to set bot's activity and print bot's username and ID once it's ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dsc.gg/thriftyhost"))
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('Bot is ready!')

# Command to display member count
@bot.command()
async def mc(ctx):
    member_count = ctx.guild.member_count
    await ctx.send(f"{member_count} Members Are In This Server.")

# Command to display user profile
@bot.command()
async def profile(ctx):
    user = ctx.author
    member_since = user.joined_at.strftime("%Y-%m-%d")
    profile_info = (
        f"Name: {user.display_name}\n"
        f"Username: {user.name}\n"
        f"ID: {user.id}\n"
        f"Discord Member Since: {member_since}\n\n"
        "Thanks For Using Me 💨"
    )
    await ctx.send(profile_info)

# Retrieve Discord bot token (you need to manually set this in CodeSandbox.io environment variables)
TOKEN = os.getenv('DISCORD_TOKEN')

# Run the bot with your Discord bot token
bot.run(TOKEN)
