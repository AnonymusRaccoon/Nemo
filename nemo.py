import traceback
from typing import Callable

import discord


class Nemo(discord.Client):
	def __init__(self, **options):
		super().__init__(**options)
		self.commands = {}
		self.reactions = []

	async def on_ready(self):
		print(f"Logged in as {self.user}.")

	async def on_message(self, message: discord.Message):
		cmd = message.content.split()
		if not any(cmd):
			return
		f = self.commands.get(cmd[0])
		if f is None:
			return
		print(f"{message.author.display_name} used the command: '{cmd[0]}'")
		try:
			await f(args=cmd[1::], message=message, guild=message.guild, channel=message.channel, member=message.author)
		except Exception:
			await message.channel.send(f"Fatal error: {traceback.format_exc()}")
			raise

	def command(self, cmd):
		def wrapper(f):
			self.commands[cmd] = f
			return f
		
		return wrapper
	
	async def on_reaction_add(self, reaction: discord.Reaction, member: discord.Member):
		if member.bot:
			return
		handler = next((x for x in self.reactions if x[0](reaction, member)), None)
		if handler is None:
			return
		try:
			await handler[1](reaction=reaction, member=member, message=reaction.message, guild=reaction.message.guild)
		except Exception:
			await reaction.message.channel.send(f"Fatal error: {traceback.format_exc()}")
			raise

	async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
		if payload.event_type != "REACTION_ADD":
			return
		
		channel: discord.TextChannel = self.get_channel(payload.channel_id)
		message: discord.Message = await channel.fetch_message(payload.message_id)
		key = f"{payload.emoji.name}:{payload.emoji.id}" if payload.emoji.id else payload.emoji.name
		reaction = discord.utils.get(message.reactions, emoji=key)
		await self.on_reaction_add(reaction, payload.member)

	def reaction(self, predicate: Callable[[discord.Reaction, discord.Member], bool]):
		def wrapper(f):
			self.reactions.append((predicate, f))
			return f
		
		return wrapper
