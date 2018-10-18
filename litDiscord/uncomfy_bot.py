import discord
from discord.ext import commands
import time
import re
import _thread

des = "this is a bot"
prefix = "!"
client = commands.Bot(command_prefix=prefix, description=des)



@client.event
async def on_message(message):
    pattern = re.compile('([\w]*[\s]*)*([Nn]*[iI1]+[gG6]+[gG6]*[eE3]+[rR]+[sS5]*)([\w]*[\s]*)*')
    def reactemoji(message):
        if message.author.name == "AstroDoge":
            emoji=discord.utils.get(client.get_all_emojis(),name='RikkaHairTwitch')
            client.add_reaction(message, emoji)

    reactemoji(message)
    if pattern.match(message.content):
        await client.delete_message(message)


client.run("NTAyNTI2NjY3NjI1ODU3MDI1.DqpPtQ._heZFO4le7dKzkCfcZL0NaUrIUo")
