import discord
from discord import NotFound

import config


def auto_delete(f):
	async def wrapper(*args, **kwargs):
		ret = await f(*args, **kwargs)
		try:
			await kwargs["message"].delete()
		except NotFound:
			pass
		return ret

	return wrapper


def event_command(f):
	async def wrapper(*args, **kwargs):
		channel: discord.TextChannel = kwargs["message"].channel
		if not channel.name[:1].isdigit():
			return None
		return await f(*args, **kwargs, event=int(channel.name[:1]))

	return wrapper


def organizer_only(f):
	async def wrapper(*args, **kwargs):
		member: discord.Member = kwargs["member"]
		channel: discord.TextChannel = kwargs["message"].channel
		event: int = kwargs["event"]
		if channel.permissions_for(member).administrator:
			return await f(*args, **kwargs)
		if any(x for x in member.roles if x.name == f"{config.ORGANIZER_PREFIX}{event}"):
			return await f(*args, **kwargs)
		return None

	return wrapper
