import discord
from discord.ext import commands
import time
import re
import _thread
import asyncio

des = "this is a bot"
prefix = "!"
client = commands.Bot(command_prefix=prefix, description=des)

@commands.has_role('Admin')
@client.command(pass_context=True)
async def timeout(ctx, args, member: discord.Member):
	pattern2 = re.compile('([0-9]*[\.]*[0-9]*)')
	if pattern2.match(args):
		await client.send_message(member, "You have been muted for: " + args + " minutes")
		allroles=member.roles
		role = discord.utils.get(member.server.roles, name='Timeout')
		for roler in allroles:
			await client.remove_roles(member, roler)
		await client.add_roles(member,role)
		await asyncio.sleep(float(args)*60)
		await client.send_message(member, "Your done now")
		await client.remove_roles(member,role)
		for roler in allroles:
			await client.add_roles(member, roler)
	else:
		await client.say("You gotta say !mute TimeInMinutes @user")
@client.event
async def on_member_join(member):
	role = discord.utils.get(memver.server.roles, name='Hooman')
	await client.add_roles(member, role);	


@client.event
async def on_message(message):
    await client.process_commands(message) 
    pattern = re.compile('([\w]*[\s]*)*([Nn]*[iI1]+[gG6]+[gG6]*[eE3]+[rR]+[sS5]*)([\w]*[\s]*)*')

    if pattern.match(message.content):
        await client.delete_message(message)
    if message.server is None:
    	await client.send_message(message.author, "Don't talk to me I'm shy")

@client.command(pass_context=True)
async def hello(ctx):
        await client.say('world')

client.run("NTAyNTI2NjY3NjI1ODU3MDI1.DqpPtQ._heZFO4le7dKzkCfcZL0NaUrIUo")
