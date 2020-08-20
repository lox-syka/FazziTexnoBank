import math
import check
				#(count_money, card_number, channel, client)
async def add_money(count, number, channel, client):
	index = open('index.txt', 'r')
	for num, line in enumerate(index, 1):
		if number in line:
			one = num - 1
	index.close()
	index = open('index.txt', 'r')
	stroka = index.read().split('\n')
	line = stroka[one].split(' | ')
	index.close()
	cards = open('cards/' + line[0], 'r')
	stroka = cards.read().split('\n')
	line_money = stroka[6]
	num_money = line_money.replace('Money: ', '')
	new_money = int(num_money) + int(count)
	cards.close()
	cards = open('cards/' + line[0], 'r')
	new_file = cards.read().replace(f'\nMoney: {num_money}', '')
	cards.close()
	f = open('cards/' + line[0], 'w')
	f.write(new_file)
	f.close()
	f = open('cards/' + line[0], 'a')
	f.write(f'\nMoney: {new_money}')
	f.close()

	number_name_message = stroka[5].replace('Name: ', '')

	suff = ''
	suff2 = ''

	staks1 = new_money / 64
	shulkers1 = new_money / 64 / 27

	staks = round(staks1)
	shulkers = round(shulkers1)

	if new_money >= 64:
		suff = f'\n   Стаков: {staks}'

	if new_money >= 1728:
		suff2 = f'\n   Шалкеров: {shulkers}'

	await channel.send(f'-- Успешно --\nНа счёт `{number_name_message}` было добавлено {count}\nСтало:\n   ИРы: {new_money}' + suff + suff2)

	server_guild = client.get_guild(725654541571326066)
	id_dis = line[0].replace('-1', '').replace('-2', '')
	member = server_guild.get_member(int(id_dis))

	await check.send(member, f'Пополнение счёта\nCумма: {count}')
	await logs_all.log(f'[] -> Пополнение: счёт[{line[0]}], Сумма[{count}], Стало[{new_money}]')

async def remove_money(count, number, channel, client, alls):
	index = open('index.txt', 'r')
	for num, line in enumerate(index, 1):
		if number in line:
			one = num - 1
	index.close()
	index = open('index.txt', 'r')
	stroka = index.read().split('\n')
	line = stroka[one].split(' | ')
	index.close()
	cards = open('cards/' + line[0], 'r')
	stroka = cards.read().split('\n')
	line_money = stroka[6]
	num_money = line_money.replace('Money: ', '')
	new_money = int(num_money) - int(count)
	cards.close()
	cards = open('cards/' + line[0], 'r')
	new_file = cards.read().replace(f'\nMoney: {num_money}', '')
	cards.close()
	if new_money >= 0:
		f = open('cards/' + line[0], 'w')
		f.write(new_file)
		f.close()
		f = open('cards/' + line[0], 'a')
		f.write(f'\nMoney: {new_money}')
		f.close()

		number_name_message = stroka[5].replace('Name: ', '')

		suff = ''
		suff2 = ''

		staks1 = new_money / 64
		shulkers1 = new_money / 64 / 27

		staks = round(staks1)
		shulkers = round(shulkers1)

		if new_money >= 64:
			suff = f'\n   Стаков: {staks}'

		if new_money >= 1728:
			suff2 = f'\n   Шалкеров: {shulkers}'

		await channel.send(f'-- Успешно --\nC счёта `{number_name_message}` было снято {count}\nСтало:\n   ИРы: {new_money}' + suff + suff2 + '\n(стаки и шалкеры округляются в меньшую сторону!)')
		server_guild = client.get_guild(725654541571326066)
		id_dis = line[0].replace('-1', '').replace('-2', '')
		member = server_guild.get_member(int(id_dis))
		await check.send(member, f'Снятие со счёта\nCумма: {count}')
		await logs_all.log(f'[] -> Снятие: счёт[{line[0]}], Сумма[{count}], Стало[{new_money}]')

	else:
		await channel.send('-- Ошибка --\nНа балансе недостаточно средств!')
		await logs_all.log(f'[ERROR] -> Снятие: счёт[{line[0]}], Сумма[{count}], Стало[NONE]')