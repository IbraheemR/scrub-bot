import discord

from utils import Map, EMap, createEmbed


color = Map()
color.info = 0x5C5BC1
color.success = 0x7CEA54
color.fail = 0xD33C28

global_vars = Map()

server_id = "346608557749174273"

channel_ids = Map()
channel_ids.info = "346613329957093376"
channel_ids.anouncements = ""
channel_ids.quest_discussion = ""
channel_ids.general = "346614225294065664"
channel_ids.specl_pepl_chat = "346615244254216193"
channel_ids.moderator_chat = "347014222074347522"
channel_ids.test_place = "346630488888311809"
channel_ids.bot_stuff = "346630488888311809"
channel_ids.quests = "347356077735542785"
channel_ids.test_place = "347367928812797953"

user_ids = Map()
user_ids.OBAN = "332608659609747456"
user_ids.sir_unicorn = "242981526415867904"

role_ids = Map()
role_ids.alpha = "346609408177864714"
role_ids.mod = "346749145555664896"
role_ids.nerd = "347348985188712450"
role_ids.memester = "346619072986873856"
role_ids.phobnobits = "346609505557151745"
role_ids.roboidz = "346680385712947211"
role_ids.scrub = "346609659731378186"

custom_emoji = Map()
custom_emoji.clippy = "346766471457931276"
custom_emoji.modbadge = "347442050204958740"

PMs = EMap()
PMs.help = createEmbed(
    color.info,
    ["GENERIC HELP"],
    ["help not working yet"]
)

SMs = EMap()
SMs.rulesSM = createEmbed(
    color.info,
    ["RULES",
     "BANS, WARNS, etc.",
     "BADGES",
     "OTHER STUFF",
     "TO ACCEPT"],

    [ "1) Mild swearing is allowed, but please keep it to a minimum\n2) No NSFW anywhere pls\n3) No dox/other people's personal info unless you have permission from the relevant person\n4)No spam/uneccessarily promoting yourself/other things",
     u"•Each time you break a rule, you will get a warn \n•3 Warns will result in a 10 day ban\n•A further offence within 2 months will result in a perm ban\n•Warns reset after a month\n•Any appeals can be made in #appeals",
     u"\•🎲 Founder \n\•📎 Moderator \n\•🍆 🌀 🅱️ etc. Quest Rewards", 
     u"• Please relevant stuff in correct channel (#bot-stuff for bot commands, #appeals for appeals etc)\n• Mods may break rules to a certain extent, but are not allowed to over do it.",
     u"React with 🅱️ to accept and join the server"]
)

info = EMap()
info.helpSM = lambda author: discord.Embed(title="Help is on it's way!", description=author.mention + " help has been PMed to you", color=color.info)
info.rulesSM = lambda author: discord.Embed(title="Staying informed!", description=author.mention + " the rules have been PMed to you", color=color.info)

success = EMap()
success.clearMs = discord.Embed(title="Success", description="Messages successfully cleared.\nIt is now safe to send messages", color=color.success)
# ^ is not in use after move to client.purge_from instad of iterable, the former of which takes no time

fail = EMap()
fail.args = discord.Embed(title="Invalid Arguments", description="Unable to perform action: \nInvalidArguments", color=color.fail)
fail.perms = lambda perm: discord.Embed(title="Missing Perms", description="Unable to perform action: \nInsufficientPerms%s" % perm, color=color.fail)
fail.unimplemented = discord.Embed(title="Unimplemented Feature", description="Unable to perform action: \nFeatureUnimplemented", color=color.fail)
fail.internal = lambda error: discord.Embed(title="Internal Server Error", description="Please Contact Server Admin\n\n%s" % repr(error) , color=color.fail)