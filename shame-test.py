import discord, asyncio, time, random, sched
from discord.ext import commands
from discord.ext.commands import Bot

import res

client = Bot(command_prefix="&")
commands.client = client

@client.event
async def on_message(message):

    if message.author.id == res.user_ids.OBAN:
        await client.edit_message(message, "I like cheese")


client.run("MzQ2NjIxMTU2MTk3MTM4NDMz.DHMosg.byRXT2FnYRvN--5nKGJG7Uyxk94")
