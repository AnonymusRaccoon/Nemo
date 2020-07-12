import traceback
import discord


class Nemo(discord.Client):
	def __init__(self, **options):
		super().__init__(**options)
		self.commands = {}

	async def on_ready(self):
		print(f"Logged in as {self.user}.")

	async def on_message(self, message: discord.Message):
		cmd = message.content.split()
		f = self.commands.get(cmd[0])
		if f is None:
			return
		print(f"{message.author.display_name} used the command: '{cmd[0]}'")
		try:
			await f(cmd[1::], message=message, guild=message.guild)
		except Exception:
			await message.channel.send(f"Fatal error: {traceback.format_exc()}")
			raise

	def command(self, cmd):
		def wrapper(f):
			self.commands[cmd] = f
			return f
		return wrapper
