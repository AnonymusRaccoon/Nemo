#!/usr/bin/env python3
import nemo
import helper
import config
import discord
from discord.ext.commands import has_permissions

number_emojis = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣"]

nemo = nemo.Nemo()


@nemo.command("!")
@has_permissions(administrator=True)
async def setup(*, message: discord.Message, guild: discord.Guild, **_):
	if any(x.name == config.CATEGORY_NAME and x.type == discord.ChannelType.category for x in guild.channels):
		return
	category = await guild.create_category(config.CATEGORY_NAME)
	organization = await guild.create_text_channel(config.ORGANIZATION_NAME, overwrites={
		guild.default_role: discord.PermissionOverwrite(send_messages=False),
		guild.me: discord.PermissionOverwrite(send_messages=True)
	}, category=category)
	await help_msg(organization)
	await message.delete()


@nemo.command("!help")
@has_permissions(administrator=True)
@helper.auto_delete
async def help_command(*, message: discord.Message, **_):
	await help_msg(message.channel)


async def help_msg(channel: discord.TextChannel):
	await channel.send(config.HELP_MSG.replace("@Me", f"<@{nemo.user.id}>"))
	await channel.send(config.EVENT_LIST)
	msg = await channel.send(config.CREATE_MSG)
	await msg.add_reaction("✅")


@nemo.reaction(lambda reaction, member: reaction.message.author.bot and config.CREATE_KEY in reaction.message.content)
async def create_event(reaction: discord.Reaction, message: discord.Message, member: discord.Member, guild: discord.Guild, **_):
	list_msg: discord.Message = [x async for x in message.channel.history() if config.LIST_KEY in x.content][0] 
	index = get_new_event_index(list_msg)
	await edit_event_status(index, config.CONFIGURING_EVENT.replace("@User", f"<@{member.id}>"), list_msg)
	await reaction.remove(member)
	
	org_role = await guild.create_role(name=f"{config.ORGANIZER_PREFIX}{index}", color=discord.Color.purple())
	await member.add_roles(org_role)
	user_role = await guild.create_role(name=f"{config.PARTICIPANT_PREFIX}{index}")
	await member.add_roles(user_role)
	channel = await guild.create_text_channel(f"{index}{config.EVENT_SUFFIX}", overwrites={
		guild.default_role: discord.PermissionOverwrite(read_messages=False),
		guild.me: discord.PermissionOverwrite(read_messages=True),
		org_role: discord.PermissionOverwrite(read_messages=True, manage_messages=True),
		user_role: discord.PermissionOverwrite(read_messages=True)
	}, category=message.channel.category)
	await list_msg.add_reaction(number_emojis[index - 1])
	await channel.send(config.SETUP_MSG)
	

def get_new_event_index(msg: discord.Message):
	for x in msg.content.split('\n'):
		if config.EMPTY_KEY in x or config.EMPTY_SLOT in x:
			return int(x[2:x.index(':')])
	last_slot = msg.content.split('\n')[-1]
	slot = int(last_slot[2:last_slot.index(':')]) + 1
	return slot if slot < 10 else -1


async def edit_event_status(index: int, text: str, list_msg: discord.Message):
	content = list_msg.content.split('\n')
	try:
		content[index + 1] = f"**{index}:** {text}"
	except IndexError:
		content.append(f"**{index}:** {text}")
	await list_msg.edit(content="\n".join(content))


if __name__ == "__main__":
	nemo.run(config.TOKEN)
