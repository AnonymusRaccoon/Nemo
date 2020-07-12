#!/usr/bin/env python3
import nemo
import helper
import config
import discord
from discord.ext.commands import has_permissions

nemo = nemo.Nemo()


@nemo.command("!")
@has_permissions(administrator=True)
async def setup(_, message: discord.Message, guild: discord.Guild, **kwargs):
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
async def help_command(_, message: discord.Message, **kwargs):
	await help_msg(message.channel)


async def help_msg(channel: discord.TextChannel):
	await channel.send(config.HELP_MSG.replace("@Me", f"<@{nemo.user.id}>"))
	msg = await channel.send(config.EVENT_LIST)
	await msg.add_reaction("🔢")
	msg = await channel.send(config.CREATE_MSG)
	await msg.add_reaction("✅")

if __name__ == "__main__":
	nemo.run(config.TOKEN)
