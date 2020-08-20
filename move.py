import os.path
import sett
import sett_l
settings = open('settings.txt', 'r')
list_s = settings.read().split('\n')
if 'true' in list_s[0]:
	development = True
	s = sett_l
else:
	development = False
	s = sett
settings.close()

async def main(suffix, number, money, author, channel):
	if_1 = os.path.exists(f'cards/{author.id}-1') # если ли первый счёт
	if_2 = os.path.exists(f'cards/{author.id}-2') # есть ли второй счёт

	if suffix == '1':
		if if_1 == True: # если есть 1 счёт
			await balance_get(suffix, number, money, author, channel)

	if suffix == '2':
		if if_2 == True: # если есть 2 счёт
			await balance_get(suffix, number, money, author, channel)
		else:
			if if_1 == True:
				await channel.send(f'{author.mention}! У вас нету счёта #2!')

	if if_1 == False:
		await channel.send(f'{author.mention}! У вас нету счётов!')


async def balance_get(suffix, number, money, author, channel):
	f = open(f'cards/{author.id}-{suffix}', 'r')
	f_list_line = f.read().split('\n')
	balance_line = f_list_line[6]
	balance_count = balance_line.replace('Money: ', '')
	balance = int(balance_count)
	print(f"Баланс: {balance}\nНадо перевести: {money}")

	if int(money) < 1:
		await channel.send(f'{author.mention}! Меньше 1{s.p} положить нельзя!')
	else:
		if balance >= int(money):
			one = "none"
			index = open('index.txt', 'r')
			for num, line in enumerate(index, 1):
				if number in line:
					one = num - 1

			if one == "none":
				await channel.send(f'{author.mention}! Счёт, не найден!\n2 args - no sreach in index.txt file!')
			index.close()
			index = open('index.txt', 'r')
			index_line = index.read().split('\n')
			index_line_number = index_line[one]
			print(index_line_number)

		else:
			await channel.send(f'{author.mention}! Недостаточно средств!')

async def move_run(one_file, two_file, count):
	f_1 = open('cards/' + one_file, 'r')
	f_2 = open('cards/' + two_file, 'r')

	f_1r = f_1.read()
	f_2r = f_2.read()

	f_1_line = f_1r.split('\n')
	f_2_line = f_2r.split('\n')

	f_1_money = f_1_line[6]
	f_2_money = f_2_line[6]

	f1_int_money = f_1_money.replace('Money: ', '')
	f2_int_money = f_2_money.replace('Money: ', '')

	f1_int = int(f1_int_money)
	f2_int = int(f2_int_money)

	print(f'БЫло\n{f1_int}\n{f2_int}\n--------------')

	new_f1 = f_1r.replace(f'\nMoney: {f1_int}', '')
	new_f2 = f_2r.replace(f'\nMoney: {f2_int}', '')

	f_1.close()
	f_2.close()

	f1 = open('cards/' + one_file, 'w')
	f2 = open('cards/' + two_file, 'w')

	f1.write(new_f1)
	f2.write(new_f2)

	f1_new_money = f1_int - count
	f2_new_money = f2_int + count

	print(f'Стало\n{f1_new_money}\n{f2_new_money}\n--------------')