#! /usr/bin/env python3

import discord
import os


class Client(discord.Client):
	async def on_ready(self):
		print(f"Logged in as {self.user}.")

	async def on_message(self):
		pass


client = Client()
client.login(os.environ["NEMO_TOKEN"])
