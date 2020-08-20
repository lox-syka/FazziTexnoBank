import os.path

async def get(author, channel):
	if_1 = os.path.exists(f'cards/{author.id}-1') # если ли первый счёт
	if_2 = os.path.exists(f'cards/{author.id}-2') # есть ли второй счёт
 
	if if_1 == True: # если есть 1 счёт
		f1 = open(f'cards/{author.id}-1')
		read1 = f1.read()
		list_read1 = read1.split('\n')
		list_test1 = list_read1[6]
		balanse1 = list_test1.replace('Money: ', '')
		name1_ = list_read1[5]
		name1 = name1_.replace('Name: ', '')

	if if_2 == True: # если есть 2 счёт
		f2= open(f'cards/{author.id}-2')
		read2 = f2.read()
		list_read2 = read2.split('\n')
		list_test = list_read2[6]
		balanse2 = list_test.replace('Money: ', '')
		name2_ = list_read2[5]
		name2 = name2_.replace('Name: ', '')

	if if_1 == False:
		await channel.send(f'{author.mention}! У вас нету счётов!')
	
	if if_2 == True: # 2 счёта
		await author.send('Балансы на счётах:\n'
							f'  Счёт #1(`{name1}`)\n'
							f'    Баланс: {balanse1}\n'
							'\n'
							f'  Счёт #2(`{name2}`)\n'
							f'    Баланс: {balanse2}')
		await channel.send(f'{author.mention}! Ваш баланс отправлен вам в ЛС.')
	else:
		if if_1 == True: # 1 счёт
			await author.send('Балансы на счётах:\n'
				f'  Счёт #1(`{name1}`)\n'
				f'    Баланс: {balanse1}\n')

			await channel.send(f'{author.mention}! Ваш баланс отправлен вам в ЛС.')

