from tkinter import *
from tkinter import ttk

root = Tk()

root.resizable(False, False)
root.title("Первая суразная GUI программа")
root.geometry("600x200")

# Функция подсчета количества вопросов
def count_of_question():
	filename = name_of_file.get()
	acces = True
	try:
		# Открываем все нужные файлы в нужных форматах
		fin = open(filename + '.txt', 'r')
	except FileNotFoundError:
		massage_ok['text'] = f'Данного файла не существует, повторите ввод'
		acces = False
	
	if acces:
		strings = fin.readlines()
		count = 0
		for string in strings:
			if '+' in string:
				count += 1

		# Очищаем поле ввода
		name_of_file.delete(0, END)
		# Выводим сообщение об успешном завршении операции
		massage_ok['text'] = f'Количество вопросов в даном файле: {count}'

# Функция обработки для конвертации вопросов с базы
def convert_basa():

	# Получаем название конечного файла с поля ввода
	filename = name_of_file.get()	

	# Запускаем счетчик для подсчета количества вопросов базы
	count_for_basa = 0

	# Открываем все нужные файлы в нужных форматах
	fin = open('basa.txt', 'r')
	fout_txt = open(filename + '.txt', 'w')
	fout_qzs = open(filename + '.qzs', 'w')
	fout_qst = open(filename + '.qst', 'w')

	# Пролучаем список всех строк читаемого файла
	strings = fin.readlines()

	# Проходим по каждой строке даного файла
	for string in strings:
		# Если в строке английская буква "А" на первом месте, ответ правильный, добавляем "+" в начало строки
		if string.find('A') == 0:
			string = '\n+' + string[3:]
		# Если в строке английская буква "В" на первом месте, ответ не правильный, добавляем "-" в начало строки 
		elif string.find('B') == 0:
			string = '-' + string[2:]
		# Если в строке английская буква "С" на первом месте, ответ не правильный, добавляем "-" в начало строки
		elif string.find('C') == 0:
			string = '-' + string[2:]
		# Если в строке английская буква "D" на первом месте, ответ не правильный, добавляем "-" в начало строки
		elif string.find('D') == 0:
			string = '-' + string[2:]
		# Если в строке английская буква "E" на первом месте, ответ не правильный, добавляем "-" в начало строки
		elif string.find('E') == 0:
			string = '-' + string[2:]
		# Если длина строки = 1, тоесть строка пуста, начинаем цикл заново
		elif len(string) == 1:
			continue
		# Если длина строки без пробелов меньше 4(учитывая табуляцию) и не равна 1 (не пустая), обрабатываем новый вопрос
		elif len(string.strip()) <= 4 and len(string) != 1:
			string = '\n?\n'
			# Продолжаем счетчик
			count_for_basa += 1
		# Во всех остальных случаях убараем перенос строки
		else:
			string = string.replace('\n', ' ')

		# Записываем обработанную строку во все файлы
		fout_txt.write(string)
		fout_qzs.write(string)
		fout_qst.write(string)
	
	# Очищаем поле ввода
	name_of_file.delete(0, END)
	# Выводим сообщение об успешном завршении операции
	massage_ok['text'] = f'Вопросы базы были успешно преобразованы: {count_for_basa} вопросов'

	# Закрываем все открытые файлы
	fin.close()
	fout_txt.close()
	fout_qst.close()
	fout_qzs.close()

# Функция обработки для конвертации вопросов с буклета
def convert_buklet():
	# Получаем название конечного файла с поля ввода
	filename = name_of_file.get()	
	
	# Запускаем счетчик для подсчета количества вопросов буклета и количества строк
	count_for_buklet = 1
	count_of_lines = 0

	# Открываем все нужные файлы в нужных форматах
	fin = open('buklet.txt', 'r')
	fout_txt = open(filename + '.txt', 'w')
	fout_qzs = open(filename + '.qzs', 'w')
	fout_qst = open(filename + '.qst', 'w')

	# Пролучаем список всех строк читаемого файла
	strings = fin.readlines()
	# Проходим по каждой строке даного файла
	for string in strings:

		# Индивидуальный индекс для всех форматов
		index = len(str(count_for_buklet)) + 3
		# Если английская буква "А" есть в строке, ответ правильный
		if 'A' in string:
			string = '\n+' + string[3:] 
		# Если английская буква "В" есть в строке, ответ неправильный
		elif 'B' in string:
			string = '-' + string[2:].lstrip()
		# Если английская буква "C" есть в строке, ответ неправильный
		elif 'C' in string and string.find('C') == 0:
			string = '-' + string[2:].lstrip()
		# Если английская буква "D" есть в строке, ответ неправильный
		elif 'D' in string:
			string = '-' + string[2:].lstrip()
		# Если английская буква "E" есть в строке, ответ неправильный
		elif 'E' in string:
			string = '-' + string[2:].lstrip()
		# Если длина строки = 1, тоесть строка пуста, начинаем цикл заново
		elif len(string) == 1:
			continue
		

		elif str(count_for_buklet) in string and len(string[:index]) == len(str(count_for_buklet)) + 3:
			string = '\n?\n' + string[index - 1:].replace('\n', '') 
			# Продолжаем счетчик
			count_for_buklet += 1

		# Логическая цепочка которая убирает лишние переносы строк
		else:
			if strings[count_of_lines - 1].find('A') == 0 or strings[count_of_lines - 1].find('B') == 0 or strings[count_of_lines - 1].find('C') == 0 or strings[count_of_lines - 1].find('D') == 0:
				string = string
			else:
				string = string.replace('\n', ' ')
		
		# Записываем обработанную строку во все файлы
		fout_txt.write(string)
		fout_qzs.write(string)
		fout_qst.write(string)
		count_of_lines += 1

	# Очищаем поле ввода
	name_of_file.delete(0, END)
	# Выводим сообщение об успешном завршении операции
	massage_ok['text'] = f'Вопросы буклета были успешно преобразованы: {count_for_buklet - 1} вопросов'

	# Закрываем все открытые файлы
	fin.close()
	fout_txt.close()
	fout_qst.close()
	fout_qzs.close()

# Функция конвертации переработаных вопросов
def convert_txt():
	# Получаем название конечного файла с поля ввода
	filename = name_of_file.get()	

	acces = True

	try:
		# Открываем все нужные файлы в нужных форматах
		fin = open(filename + '.txt', 'r')
	except FileNotFoundError:
		massage_ok['text'] = f'Данного файла не существует, повторите ввод'
		acces = False

	if acces:
		fin_qzs = open(filename + '.qzs', 'w')
		fin_qst = open(filename + '.qst', 'w')

		# Перезаписываем файлы
		fin_qzs.write(fin.read())
		fin = open(filename + '.txt', 'r')
		fin_qst.write(fin.read())

	# Закрываем все открытые файлы
	fin.close()
	fin_qst.close()
	fin_qzs.close()

	# Очищаем поле ввода
	name_of_file.delete(0, END)
	# Выводим сообщение об успешном завршении операции
	massage_ok['text'] = f'Конвертация была проведена успешно'


# Охарактеризовываем строку для ввода даных
first_massage = Label(root, text='Введите имя для файла')
first_massage.pack()

# Строка для ввода данных
name_of_file = Entry(root, width=30)
name_of_file.pack()
name_of_file.focus_set()

# Кнопка для конвертации вопросов базы
btn_start_for_basa = ttk.Button(root, text='Запустить для базы', command=convert_basa)
btn_start_for_basa.pack()

# Кнопка для конвертации вопросов буклета
btn_start_for_buklet = ttk.Button(root, text='Запустить для буклетов', command=convert_buklet)
btn_start_for_buklet.pack()

# Кнопка для конвертации переработаных вопросов
btn_start_for_buklet = ttk.Button(root, text='Конвертировать формат', command=convert_txt)
btn_start_for_buklet.pack()

# Кнопка для конвертации переработаных вопросов
btn_count_of_question = ttk.Button(root, text='Подсчитать количество вопросов', command=count_of_question)
btn_count_of_question.pack()

# Сообщение об успешном завершении конвентации
massage_ok = Label(root)
massage_ok.pack()

root.mainloop()