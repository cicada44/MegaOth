from mega import *
from datetime import datetime
import time
from colorama import *

init()

mega = Mega()

global login
global password

print(" __  __                   ___  _   _")     
print("|  \\/  | ___  __ _  __ _ / _ \| |_| |__")  
print("| |\\/| |/ _ \\/ _` |/ _` | | | | __| '_ \\") 
print("| |  | |  __/ (_| | (_| | |_| | |_| | | |")
print("|_|  |_|\\___|\\__, |\\__,_|\\___/ \\__|_| |_|")
print("              |___/                       ")

try:
    login = input('[!] Введите логин: ')
    password = input('[!] Введите пароль: ')
except:
    print('[!!!] Что то не так!')

try:
	if login == None or login == '' or password == None or password == '':
		print('\n[!!!] Что то пошло не так')
	else:
		mega.login(str(login), str(password))
		print('[+] Аутентификация прошла успешно!')
except:
	print('[!!!] Неправильный логин или пароль')
	print('[Bye] Выход из программы...')
	time.sleep(2.0)
	exit()

menu = (Fore.GREEN + '----- Функции ----- \n'
		'[1] Информация пользователя\n'
		'[2] Баланс\n'
		'[3] Свободное место на аккаунте\n'
		'[4] Поиск папки или файла\n'
		'[5] Добавление файла\n'
		'[6] Создание папки\n'
		'[7] Удаление файла\n'
		'[8] Переименование файла\n'
		'[9] Добавление файлов на экспорт\n')

print(menu.center(24))

print('')

def Backup():

	try:

		command = input('[?] Какую функцию задействовать: ')

		print('')
	
		if command == None or command == '':
			print('[!!!] Введена пустая строка!')

			print('')

		elif int(command) == 1:

			try:
				details = mega.get_user()
				print('[+] Ваши данные: ')
				print('')
				login = details['email']
				print('Login - {}'.format(login))
				name = details['name']
				print('Name - {}'.format(name))
	
			except:
				print('[!!!] Что то не так!')
				print('')
	
		elif int(command) == 2:
	
			try:
				balance = mega.get_balance()
				if len(balance) == 0:
					print('[+] Ваш баланс - 0')
					print('')
				else:
					print('[+] Ваш баланс - {}'.format(balance))
					print('')
			except:
				print('[!!!] Что то не так!')
				print('')
	
		elif int(command) == 3:
	
			try:
				space = mega.get_storage_space(kilo=True)
				used_space = space['used']
				total_space = space['total']
				free_space = int(total_space) - int(used_space)
				mgb_used_space = int(used_space) // 1024
				mgb_total_space = int(total_space) // 1024
				mgb_free_space = int(free_space) // 1024
				ggb_used_space = int(mgb_used_space) // 1024
				ggb_total_space = int(mgb_total_space) // 1024
				ggb_free_space = int(mgb_free_space) // 1024
				print('[!] Всего ~ {}MB, ~ {}GB'.format(mgb_total_space, ggb_total_space))
				print('[!] Использовано ~ {}МB, ~ {}GB'.format(mgb_used_space, ggb_used_space))
				print('[!] Свободно ~ {}МB, ~ {}GB'.format(mgb_free_space, ggb_free_space))
				print('')
			except:
				print('[!!!] Что то не так!')
				print('')
	
		elif int(command) == 4:
	
			folder_for_find = input('[?] Введие имя папки или файла, которую хотите найти: ')
			print('')
	
			if folder_for_find == None or folder_for_find == '':
				print('[!!!] Введена пустая строка!')
				print('')
	
			else:
	
				try:
	
					cm = input('[?] Искать в удаленных (x/y)? ')
					print('')
	
					if cm == None or cm == '':
	
						print('[!!!] Введена пустая строка!')
						print('')
	
					elif cm == 'y':
	
						folder = mega.find(folder_for_find, exclude_deleted=True)
						
						if folder != None:
							print('[+] Найдено!')
							print('')
						else:
							print('[!] Не найдено!')
							print('')
	
					elif cm == 'n':
	
						folder = mega.find(folder_for_find)
						
						if folder != None:
							print('[+] Найдено!')
							print('')
						else:
							print('[!] Не найдено!')
							print('')
	
					else:
	
						print('[!!!] Неизвестная команда!')
						print('')
	
				except:
					print('[!!!] Что то не так!')
					print('')
	
		elif int(command) == 5:
	
			way_of_file = input('[?] Введите путь к файлу: ')
			print('')
	
			if way_of_file == None or way_of_file == '':
				print('[?] Введена пустая строка')
				print('')
	
			else:
	
				try:
					upload_file = mega.upload(way_of_file)
					print('[+] Успешно!')
					print('')
	
					q = input('[?] Получить ссылку на этот файл (y/n)? ')
					print('')
	
					if q == None or q == '':
	
						print('[!!!] Введена пустая строка!')
						print('')
	
					elif q == 'y':
	
						link_upload_file = mega.get_upload_link(upload_file)
	
						print('[!] Ссылка: {}'.format(link_upload_file))
						print('')
	
					elif q == 'n':
	
						return ''
	
					else:
						print('[!!!] Введена неизвестная команда!')
						print('') 

				except:
					print('[!!!]Неверно указан путь к файлу')
					print('')
	
		elif int(command) == 6:
	
			global name_of_folder
	
			name_of_folder = input('[?] Введите название папки: ')
			print('')
	
			if name_of_folder == None or name_of_folder == '':
	
				print('[!!!] Введена пустая строка!')
				print('')
	
			else:
	
				try:
					mega.create_folder(name_of_folder)
					print('[+] Успешно!')
					print('')
				except:
					print('[!!!] Что то не так!')
					print('')
	
		elif int(command) == 7:
	
			file_for_find = input('[?] Введите имя файла: ')
			print('')
	
			if file_for_find == None or file_for_find == '':
	
				print('[!!!] Введена пустая строка!')
				print('')
	
			else:
	
				try:
					file = mega.find(file_for_find)
					if file != None:
						print('[+] Файл найден!')
						print('')
					elif type(file) == None:
						print('[!] Файл не найден!')
						print('')
				except:
					print('[!!!] Что то не так!')
					print('')		
				try:
					mega.delete(file[0])
					print('[+] Файл успешно удалён!')
					print('')
				except:
					print('[!!!] Что то не так!')
					print('')
	
		elif int(command) == 8:
	
			name_of_file = input('[?] Название файла, который вы хотите переименовать: ')
			print('')

			name_final = input('[?] Название, в которое вы хотите переименовать файл: ')
			print('')
	
			if name_of_file == None or name_of_file == '' or name_final == None or name_final == '':
	
				print('[!!!] Введена пустая строка!')
				print('')
	
			else:
	
				try:
					file_for_find = mega.find(str(name_of_file))
					print('[+] Файл найден!')
					print('')
				except:
					print('[!] Файл не найден!')
					print('')
		
				try:
					mega.rename(file_for_find, name_final)
					print('[+] Файл успешно переименован!')
					print('')
				except:
					print('[!!!] Что то не так!')
					print('')
	
		elif int(command) == 9:
	
			file_for_export = input('[?] Введите имя экспортируемого фала: ')
	
			if file_for_export == None or file_for_export == '':

				print('[!!!] Введена пустая строка')
				print('')
	
			else:
	
				try: 
					mega.find(str(file_for_export))
					print('[+] Успешно!')
					print('')
				except:
					print('[!] Данного файла не существует!')
					print('')
	
				try:
					public_exported_web_link = mega.export(str(file_for_export))
					print('[+] Успешно')
					print('')
					print('[!] Ссылка: {}'.format(public_exported_web_link))
					print('')
				except:
					print('[!!!] Что то не так!')
					print('')
	
		else:
	
			print('\n[!!!] Введена неизвестная команда!')
			print('')

		def Reload():

			while  True:
	
				rel = input('[?] Работать с программой ещё раз (y/n)? ')
				print('')
	
				if rel == 'y':
	
					Backup()
	
					break
	
				elif rel == 'n':
	
					print('[Bye] Выход из программы...')
					print('')
					exit()
	
					break
	
				else:
					print('\n[!!!] Неизвестная команда! Выход из программы ...')
					print('')
	
					time.sleep(2.0)
	
					exit()

		Reload()
		
	except ValueError:
	    
	    print(Fore.RED + '\n[Bye] Неизвестная команда! Выход из программы...')
	    time.sleep(2.0)
	    exit()

	except KeyboardInterrupt:

		print(Fore.RED + '\n'
			'[Bye] Выход из программы ...')

		time.sleep(2.0)

		exit()

Backup()

