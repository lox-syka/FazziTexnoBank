import os.path
import os
import random
import sett
import sett_l
import logs_all

settings = open('settings.txt', 'r')
list_s = settings.read().split('\n')
if 'true' in list_s[0]:
	development = True
	s = sett_l
else:
	development = False
	s = sett
settings.close()

async def remove(number, logs):
	index = open('index.txt', 'r')
	for num, line in enumerate(index, 1):
		if number in line:
			one = num - 1
	index.close()

	index = open('index.txt', 'r')
	card_file_text = index.read()

	i_list_stroka = card_file_text.split('\n')
	i_list_line = i_list_stroka[one]
	done_line = i_list_line.split(' | ')

	cardd = open('cards/' + done_line[0])
	cardd_read = cardd.read()
	cardd.close()

	print(i_list_line)
	print(done_line[0])
	os.remove('cards/' + done_line[0])

	if s.debug == 0:
		print(card_file_text)

	new_index_text = card_file_text.replace(f'{i_list_line}\n', '')
	index.close()
	f = open('index.txt', 'w')
	f.write(new_index_text)
	f.close()

	log = cardd_read.replace('\n', '\\n')
	await logs_all.log(f'[File] - [Delete \'{done_line[0]}\'] -> удалён счёт! Файл карты: "{log}"')
	await logs.send(f'Удаление счёта!\nФайл карты:\n`{cardd_read}`\n---------\nУдалённая линия в индеке:\n`{i_list_line}`\nНомер строки индекса(`{one}`(+1))')

async def create(nick, dis, channel, card_name, mention, discord, logs):
	if_1 = os.path.exists(f'cards/{dis}-1') # если ли первый счёт
	if_2 = os.path.exists(f'cards/{dis}-2') # есть ли второй счёт
 
	if if_1 == False: # если нету 1 счёт
		await card_generate(dis, nick, '1', card_name, channel, mention, discord, logs)
	else: # если есть 1 счёт
		if if_2 == False: # если нету 2 счёт
			await card_generate(dis, nick, '2', card_name, channel, mention, discord, logs)
		else:
			await logs_all.log(f'[ERROR] - привышен лимит счётов, остановка.')
			await channel.send('-- Ошибка --\nУ данного человека уже есть максмальное количество счётов!')


async def card_generate(dis, nick, suffix, card_name, channel, mention, discord, logs):
	file_name = f'{dis}-{suffix}'
	number = f'{(random.randint(1000, 9999))}_{(random.randint(1000, 9999))}' # создание номера счёта
	cvc = (random.randint(100, 999)) # создание CVC кода
	pin_code = (random.randint(1000, 9999)) # создание ПИН кода
	discord_id = dis
	minecraft_nick = nick

	await new_file(file_name, number, cvc, pin_code, discord_id, minecraft_nick, card_name)
	await index(file_name, number, cvc, pin_code, discord_id, minecraft_nick, card_name)

	two_identify = suffix.replace('-', '')

	await channel.send('Данные созданного счёта были отправлены владельцу счёта!')
	await channel.send(f'Скопируйте эти данные в книжку на 1 страницу!\n'
						f'```\n-------------------\n'
						f'\n'
						f'   {number}\n'
						f'\n'
						f'{minecraft_nick}\n'
						f'\n'
						f'Вторичный номер: #{two_identify}\n'
						f'-------------------\n'
						f'\n'
						f'\n'
						f'\n'
						f'\n'
						f'© Фаззи\n'
						f'© ТехноБанк```\n\n'
						f'На вторую страницу скопируйте это: `CVC: {cvc}`\nНазавите книгу `Банковская карточка` и подпишите!\nПосле подписи кники отдайте книгу владельцу счёта!')

	embed=discord.Embed(title="Новый счёт!", description=f"На ваш дискорд аккаунт был создан счёт #{suffix.replace('-', '')}", color=0x0aff12)
	embed.add_field(name="Номер счёта", value=number, inline=True)
	embed.add_field(name="CVC", value=f'||{cvc}||', inline=True)
	embed.add_field(name="PIN-code", value=f'||{pin_code}||', inline=True)
	embed.add_field(name="Ник на сервере", value=minecraft_nick, inline=True)
	embed.add_field(name="Название счёта", value=card_name, inline=True)
	embed.add_field(name="Баланс", value='0', inline=True)
	embed.set_footer(text="(c) Фаззи\n(c) ТехноБанк")
	await mention.send(embed = embed)

	dess =  (f'Номер: `{number}`\n'
			f'CVC: ||{cvc}||\n'
			f'Pin_code: ||{pin_code}||\n'
			f'Ник: `{minecraft_nick}`\n'
			f'Название: `{card_name}`\n'
			f'Название файла: {file_name}\n'
			f'Suffix: {suffix}\n'
			f'Владелец: {mention.mention}')

	embed=discord.Embed(title='Создание счёта!', description=dess, color=0x0aff12)
	await logs.send(embed = embed)

async def new_file(file_name, number, cvc, pin_code, discord_id, minecraft_nick, card_name):
	f = open(f'cards/{file_name}', 'w')

	wwww = (f'Number: {number}\n'
			f'Cvc: {cvc}\n'
			f'Pin_code: {pin_code}\n'
			f'Owner_discord: {discord_id}\n'
			f'Owner_game: {minecraft_nick}\n'
			f'Name: {card_name}\n'
			f'Money: 0')

	f.write(wwww)

	f.close()

	log = wwww.replace('\n', '\\n')
	await logs_all.log(f'[File] [{file_name}, \'w\'] -> "{log}"')

async def index(file_name, number, cvc, pin_code, discord_id, minecraft_nick, card_name):
	f = open(f'index.txt', 'a')

	www = (f'{file_name} | '
		f'{number} | '
		f'{cvc} | '
		f'{pin_code} | '
		f'{discord_id} | '
		f'{minecraft_nick} | '
		f'{card_name}\n')

	f.write(www)

	f.close()

	log = www.replace('\n', '\\n')

	await logs_all.log(f'[File] [index.txt, \'a\'] -> "{log}"')