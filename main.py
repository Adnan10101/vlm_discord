import discord 
from discord.ext import commands
import bot.discord_frontend
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)

if __name__ == "__main__":
    bot.discord_frontend(bot)
    bot.run(TOKEN)