import discord, asyncio, time, random, sched
from discord.ext import commands
from discord.ext.commands import Bot

import res, utils, log, commands


client = Bot(command_prefix="&")
commands.client = client

@client.event
async def on_ready():
    try:

        await client.change_presence( game=discord.Game(name="&help"))

        await commands.setup_accept(client.get_channel(res.channel_ids.rules))

        commands.server = client.get_server(res.server_id)

    except Exception as error:
        await client.send_message(client.get_channel(res.channel_ids.general), embed=res.fail.internal(error))
        raise e

@client.event
async def on_message(message):
    try:

        c = message.content

        isCommand = True if c.startswith("&") else False

        if isCommand and not message.author.bot:
            c = c[1:].lower()

            command, *keywords = c.split(" ")

            try:
                if   command == "ping":    await commands.ping(message, keywords)
                elif command == "error":   await commands.error(message, keywords)
                elif command == "rules":   await commands.rules(message, keywords)
                elif command == "help":    await commands.help_(message, keywords)
                elif command == "badge":   await commands.badge(message, keywords)
                elif command == "clear":   await commands.clear(message, keywords)
                elif command == "clense":  await commands.clense(message, keywords)
                elif command == "spamme":  await commands.spamme(message, keywords)
                elif command == "balance": await commands.balance(message, keywords)
                elif command == "give":    await commands.give(message, keywords)

            except utils.ArgumentError as error:
                await commands.send_arg_error(message, error)

            except utils.PermissionError as error:
                await commands.send_perm_error(message, error)

            except utils.Unimplemented as error:
                await commands.send_unimplemented_error(message, error)

    except Exception as error:
        await client.send_message(message.channel, embed=res.fail.internal(error))
        log.log("-1", repr(error))
        raise error

@client.event
async def on_reaction_add(reaction, user):
    try:

        if (reaction.emoji == u"🅱") and (reaction.message.id == res.global_vars.accept_id) and (not user.bot) and (len(user.roles) == 1):
            await commands.accept(user)

    except Exception as error:
        await client.send_message( client.get_channel(res.channel_ids.general), embed=res.fail.internal(error) )
        raise e


client.run("MzQ2NjIxMTU2MTk3MTM4NDMz.DHMosg.byRXT2FnYRvN--5nKGJG7Uyxk94")
