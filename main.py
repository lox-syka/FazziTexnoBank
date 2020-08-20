import discord
import tarfile
import sett
import sett_l
import cards_
import os
import money
import balence
import move
from discord import File
import all_numbers
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

print("Development: " + str(development))

class MyClient(discord.Client):
	async def on_ready(self):
		print(f'"{client.user.name}" Started')
		global ll_ogs
		ll_ogs = client.get_channel(s.logs)
		await ll_ogs.send('Бот запущен ._.\nКонсоль:\n'
							f'     `"{client.user.name}" Started`', file = File('all.log'))
		#global log_file
		log_file = open('all.log', 'w')
		log_file.write('')
		log_file.close()
		await logs_all.log('[] [] [FAZZI BANK] [] []\nЛОГИ ТЕХНОБАНКА.\n\n[bot] -> bot started!')
		


	async def on_message(self, message):
		if message.content.startswith('!'):
			logs_t = (f'[Command] - [{message.channel.name}] - [{message.author.name}#{message.author.discriminator}] -> {message.content}')
			await logs_all.log(logs_t)
		else:
			if message.author.id == client.user.id:
				pass
			else:
				logs_t = (f'[Message] - [{message.channel.name}] - [{message.author.name}#{message.author.discriminator}] -> {message.content}')
				await logs_all.log(logs_t)

		a = message.content.split(' ')
		author = message.author
		channel = message.channel

		if message.channel.id == s.channel_all: # если канал #участники
			if a[0] == '!баланс':
				try:
					author = message.author
					channel = message.channel
					await balence.get(author, channel)
					await logs.main(ll_ogs, 'Запрос баланса', f'{message.author.mention} запросил баланс')

				except IndexError:
					await message.channel.send(s.error_syntacs)
				except discord.errors.Forbidden:
					await message.channel.send('Ошибка, у вас закрыты личные сообщения.')
	
			if a[0] == '!перевод':
				await message.channel.send(f'Ошибка, для перевода деняг подойдите к банкиру.')
	
			if a[0] == '!список':
				if a[1] == 'карт':
					try:
						await all_numbers.main(message)
					except discord.errors.Forbidden:
						await message.channel.send('Ошибка, у вас закрыты личные сообщения.')
	
				return

		if message.channel.id == s.channel_bankir: # если канал банкир
			if str(s.bankir) in str(author.roles): # если банкир
				if a[0] == '!создать':
					if a[1] == 'счёт':
						ban_list = [726022503629324298, 235088799074484224, 228537642583588864, 731780392549351444]
						try:
							nick = a[2]
							mention = message.mentions[0]
							dis = mention.id
							card_name = a[3]
							if str(dis) in str(ban_list):
								await message.channel.send('Ошибка, `{error.no_created.banned_list}`')
								await logs_all.log(f'[ERROR] -> Акк в БАН листе -> !создать счёт')
							else:
								mess_test = await mention.send('Создание счёта.')
								await mess_test.delete()
								await cards_.create(nick, dis, channel, card_name, mention, discord, ll_ogs)
								

						except IndexError:
							await message.channel.send(s.error_syntacs)
						except discord.errors.Forbidden:
							await message.channel.send('Критическая ошибка, у будующего владельца счёта закрыты личные сообщения в Дискорд, данные отправить не удалось!\nОперация отменена.')
							await logs_all.log(f'[ERROR] -> закрыты ЛС -> !создать счёт')

				if a[0] == '!положить':
					try:
						count_money = a[2]
						card_number = a[1]
						channel = message.channel
						await money.add_money(count_money, card_number, channel, client)
					except IndexError:
						await message.channel.send(s.error_syntacs)

				if a[0] == '!снять':
					try:
						if str(732261445873434756) in str(author.roles):
							alls = True
						else:
							alls = False

						card_number = a[1]
						channel = message.channel
						await money.remove_money(count_money, card_number, channel, client, alls)
					except IndexError:
						await message.channel.send(s.error_syntacs)



		if a[0] == '!debug':
			if '725658167517642753' in str(author.roles):
				if a[1] == 'delete_number':
					card_number = a[2]
					await cards_.remove(card_number, ll_ogs)
					await logs_all.log(f'[debug] - [delete_number] -> Процес пошёл.')

				if a[1] == 'move_run':
					await move.move_run('725663873625227294-1','725663873625227294-2', 1)

				if a[1] == 'backup':
					await message.channel.send(file = File('index.txt'))
					tar = tarfile.open("backup.gz", "w:gz")
					tar.add("cards", arcname="cards")
					tar.add("index.txt", arcname="index.txt")
					tar.close()
					await message.channel.send('Бэкап данных успешно создан и отправлен, в архиве backup.gz есть все необходимые файлы для востановления счётов. Бэкап данных бота - `!debug backup_bot`', file = File('backup.gz'))
					await logs_all.log(f'[debug] - [backup] -> Бекап успешен.')

				if a[1] == 'backup_bot':
					tar = tarfile.open("backup_bot.gz", "w:gz")
					tar.add("./", arcname="bot_files")
					tar.close()
					await message.channel.send('Полный бэкап данных. тут и файлы бота и файлы карт.', file = File('backup_bot.gz'))
					await logs_all.log(f'[debug] - [backup_bot] -> Бекап успешен.')

				if a[1] == 'file_read':
					try:
						filee = a[2]
						file_text = open(filee, 'r')
						await message.channel.send('```' + file_text.read() + '```', file = File(filee))
					except discord.errors.HTTPException:
						await message.channel.send('Файл слишком большой для read, файл был просто отправлен!', file = File(filee))
					except IndexError:
						await message.channel.send(s.error_syntacs)
					except FileNotFoundError:
						await message.channel.send('Файл не найден')

				if a[1] == 'listdir':
					try:
						await message.channel.send('```\n' + str(os.listdir(a[2])) + '```')
					except IndexError:
						await message.channel.send(s.error_syntacs)
					except FileNotFoundError:
						await message.channel.send('Деректория не найдена')
					except discord.errors.HTTPException:
						await message.channel.send('Много файлов! сообщение получаеться больше 2000 символов(максимальный размер сообщения)')

				if a[1] == 'user_send':
					men = message.mentions[0]
					kow_list = message.content.split('"')
					await men.send(str(kow_list[1]))
					await logs_all.log(f'[debug] - [user_send] -> "{kow_list[1]}"')


client = MyClient()
if development == False:
	client.run(s.tok)
else:
	client.run('NzI2MDIyNTAzNjI5MzI0Mjk4.XvXQgA.Xft9sufFZnZSqGC_Fm3o8Qy3ybo')