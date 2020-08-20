# чек о действии
import discord

async def send(member, text):
	embed=discord.Embed(title="Чек.", description=text, color=0x0aff12)
	await member.send(embed = embed)