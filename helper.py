def auto_delete(f):
	async def wrapper(*args, **kwargs):
		ret = await f(*args, **kwargs)
		await kwargs["message"].delete()
		return ret

	return wrapper

