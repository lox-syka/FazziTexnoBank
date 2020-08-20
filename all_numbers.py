import discord
import os.path

async def main(message):
	if_1 = os.path.exists(f'cards/{message.author.id}-1') # если ли первый счёт
	if_2 = os.path.exists(f'cards/{message.author.id}-2') # есть ли второй счёт

	f1_r = ''
	f2_r = ''

	if if_1 == True: # если есть 1 счёт
		f1 = open(f'cards/{message.author.id}-1', 'r')
		f1_r = f1.read()
		list_1 = f1_r.split('\n')

		number1 = list_1[0].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		cvc1 = list_1[1].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		pin_code1 = list_1[2].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		minecraft_nick1 = list_1[4].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		card_name1 = list_1[5].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		money1 = list_1[6].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')

		f1_e=discord.Embed(title="Список счётов! #1", description=f"Это счёт #1", color=0x0aff12)
		f1_e.add_field(name="Номер счёта", value=number1, inline=True)
		f1_e.add_field(name="CVC", value=f'||{cvc1}||', inline=True)
		f1_e.add_field(name="PIN-code", value=f'||{pin_code1}||', inline=True)
		f1_e.add_field(name="Ник на сервере", value=minecraft_nick1, inline=True)
		f1_e.add_field(name="Название счёта", value=card_name1, inline=True)
		f1_e.add_field(name="Баланс", value=money1, inline=True)
		f1_e.set_footer(text="(c) Фаззи\n(c) ТехноБанк")
		await message.author.send(embed = f1_e)

	if if_2 == True: # если есть 2 счёт
		f2 = open(f'cards/{message.author.id}-2', 'r')
		f2_r = f2.read()
		list_2 = f2_r.split('\n')

		number2 = list_2[0].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		cvc2 = list_2[1].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		pin_code2 = list_2[2].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		minecraft_nick2 = list_2[4].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		card_name2 = list_2[5].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')
		money2 = list_2[6].replace('Number: ', '').replace('Pin_code: ', '').replace('Cvc: ', '').replace('Owner_game: ', '').replace('Name: ', '').replace('Money: ', '')


		f2_e=discord.Embed(title="Список счётов! #2", description=f"Это счёт #2", color=0x0aff12)
		f2_e.add_field(name="Номер счёта", value=number2, inline=True)
		f2_e.add_field(name="CVC", value=f'||{cvc2}||', inline=True)
		f2_e.add_field(name="PIN-code", value=f'||{pin_code2}||', inline=True)
		f2_e.add_field(name="Ник на сервере", value=minecraft_nick2, inline=True)
		f2_e.add_field(name="Название счёта", value=card_name2, inline=True)
		f2_e.add_field(name="Баланс", value=money2, inline=True)
		f2_e.set_footer(text="(c) Фаззи\n(c) ТехноБанк")
		await message.author.send(embed = f2_e)

	if if_1 == False:
		await message.channel.send(f'{message.author.mention}! У вас нету счётов!')
	else:
		await message.channel.send(f'{message.author.mention}! Список ваших счётов отправлен вам в ЛС.')
