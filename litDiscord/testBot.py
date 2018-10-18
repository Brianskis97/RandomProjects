import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone
from pytz import all_timezones
import re

des = "this is a bot"
prefix = "!"
client = commands.Bot(command_prefix=prefix, description=des)
@client.event
async def on_event():
	print("Logged in as:")
	print(client.user.id)
@client.command(pass_context=True)
async def hello(ctx):
	await client.say('world')
@client.command(pass_context=True)
async def repeat(ctx, arg):
	await client.say(arg)
@client.command(pass_context=True)
async def listUsers(ctx):
	for each in client.get_all_members():
		await client.say(each)
@client.command(pass_context=True)
async def who(ctx, name):
	pinger = '<@' + ctx.message.author.id + '>'
	await client.say(pinger)
@client.command(pass_context=True)
async def when(ctx):
	await client.say(time.strftime("%I:%M:%S"))
@client.command(pass_context=True)
async def zone(ctx, arg):
	test = ""
	for each in all_timezones:
		if arg in each:
			test += each + "\n"
	await client.say(test)
@client.command(pass_context=True)
async def requestAll(ctx):
	test={}
	for i in range(len(all_timezones)):
        	test[i] = ""

	for i in range(len(all_timezones)):
        	test[i//100] += all_timezones[i] + "\n"
	for i in range(len(test)):
		await client.send_message(ctx.message.author, test[i])
@client.command(pass_context=True)
async def REE(ctx):
        await client.say("fuck you")
@client.event
async def on_message(message):
    pattern = re.compile('([\w]*[\s]*)*([Nn]*[iI1]+[gG6]+[gG6]*[eE3]+[rR]+[sS5]*)([\w]*[\s]*)*')
    if message.author.name == "AstroDoge":
        emoji=discord.utils.get(client.get_all_emojis(),name='RikkaHairTwitch')
        await client.add_reaction(message, emoji)
    if pattern.match(message.content):
        await client.delete_message(message)


client.run('NDE1MjkxOTI1NTkyMjc3MDAz.DWzysQ.pbv41Qou7U3Et1cBulM_YDwN8Hw')


