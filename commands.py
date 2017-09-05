import discord, asyncio, time, random

import utils, res, log

client = None
server = None


async def setup_accept(channel):
    await client.purge_from(channel)
    msg = await client.send_message(channel, embed=res.SMs.rulesSM())
    await client.add_reaction(msg, u"🅱")

    res.global_vars.accept_id = msg.id

async def accept(user):
    role = discord.utils.find(lambda r: r.id == res.role_ids.scrub, server.roles)
    await client.add_roles(user, role)



async def ping(message, keywords):
    await client.send_message(message.channel, "P%sng!" % random.choice("aeouy"))

async def error(message, keywords):
    if message.channel.permissions_for(message.author).administrator:
        raise Exception
    else:
        raise utils.PermissionError("permissions.administrator", message)

async def rules(message, keywords):
    await client.send_message(message.author, embed=res.PMs.rules())
    await client.send_message(message.channel, embed=res.info.rulesSM(message.author))

async def help_(message, keywords):
    await client.send_message(message.author, embed=res.PMs.help())
    await client.send_message(message.channel, embed=res.info.helpSM(message.author))

async def badge(message, keywords):
    if message.channel.permissions_for(message.author).administrator:
        try:
            badge = keywords[0]
            user_id = ''.join(filter(lambda x: x.isdigit(), keywords[1]))

            user = server.get_member(user_id)

            nick  = user.nick if user.nick else user.name

            await client.change_nickname(user, badge + nick)

            log.log(0, "Gave user @%s:%s bdage %s " % (user.name, user.id, badge))

        except (IndexError, AttributeError):
            raise utils.ArgumentError(None, message)
    else:
        raise utils.PermissionError("permissions.administrator", message)

async def clear(message, keywords):
    if message.channel.permissions_for(message.author).manage_messages:
        try:
            amount = 100
            try:
                amount = int(keywords[0])

            except IndexError:
                pass

            if amount <= 0:
                raise ValueError

            await client.purge_from(message.channel, limit=amount+1)

            log.log(0, "Cleared %s messages from channel #%s:%s, at request of @%s:%s" % (amount, message.channel.name, message.channel.id, message.author.name, message.author.id))

        except (ValueError):
            raise utils.ArgumentError(None, message)
    else:
        raise utils.PermissionError("permissions.manage_messages", message)

async def clense(message, keywords):
    if message.channel.permissions_for(message.author).manage_messages:
        try:
            amount = 100
            try:
                amount = int(keywords[0])

            except IndexError:
                pass

            if amount <= 0:
                raise ValueError

            await client.purge_from(message.channel, limit=amount+1, check=lambda m: m.author.bot or m.content.startswith("&"))

            log.log(0, "Clensed %s messages from channel #%s:%s, at request of @%s:%s" % (amount, message.channel.name, message.channel.id, message.author.name, message.author.id))

        except (ValueError):
            raise utils.ArgumentError(None, message)
    else:
        raise utils.PermissionError("permissions.manage_messages", message)

async def shame(message, keywords):
    pass

async def spamme(message, keywords):

    try:
        amount = 100
        try:
            amount = int(keywords[0])

        except IndexError:
            pass

        if amount <= 0:
            raise ValueError

        for i in range(amount):
            await client.send_message(message.author, ":b:"*100)

        log.log(0, "Spamming @%s:%s with %s messages (:b: * 100)" % (message.author.name, message.author.id, amount))


    except (IndexError, AttributeError, ValueError):
        raise utils.ArgumentError(None, message)



async def balance(message, keywords):
    raise utils.Unimplemented(None, message)

async def give(message, keywords):
    raise utils.Unimplemented(None, message)




async def send_arg_error(message, error):
    await client.send_message(message.channel, embed=res.fail.args())
    log.log(2, "User @%s:%s raised error utils.ArgumentError (Attempted \"%s\")" % (error.args[1].author.name, error.args[1].author.id, error.args[1].content))

async def send_perm_error(message, error):
    await client.send_message(message.channel, embed=res.fail.perms(error.args[0]))
    log.log(2, "User @%s:%s raised error utils.PermissionError (Attempted \"%s\")" % (error.args[1].author.name, error.args[1].author.id, error.args[1].content))

async def send_unimplemented_error(message, error):
    await client.send_message(message.channel, embed=res.fail.unimplemented())
