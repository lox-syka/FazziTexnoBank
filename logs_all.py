from datetime import datetime


async def log(text):
	log_file = open('all.log', 'a')
	time = datetime.strftime(datetime.now(), '%H:%M:%S')
	log_file.write(f'[{time}] - {text}\n')
	log_file.close()