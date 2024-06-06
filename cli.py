# Словарь для кодировки
DICTIONARY = {  'А':'.-', 'Б':'-...','В':'.--', 
                'Г':'--.', 'Д':'-..',
                'Е':'.', 'Ж':'...-', 
                'З':'--..','И':'..', 
                'Й':'.---', 'К':'.-.',
                'Л':'.-..', 'М':'--',
                'Н':'-.','О':'---', 
                'П':'.--.', 'Р':'.-.',
                'С':'...', 'Т':'-', 'У':'..-',
                'Ф':'..-.', 'Х':'....', 
                'Ц':'-.-.','Ч':'---.',
                'Ш':'----', 'Щ':'--.-',
                'Ъ':'.--.-.','Ы':'-.--',
                'Ь':'-..-','Э':'...-...',
                'Ю':'..--', 'Я':'.-.-',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ': "   ", '!': '-.-.--'
                }
# Словарь для  декодировки
DICTIONARY_REVERSED = {value: key for key, value in DICTIONARY.items()}

import decode, code_1
from datetime import datetime

# Цикл для повторение программы без перезапуска
while True:

    # Выбор режима работы код/декод
    print("Выберите режим программы")
    print('1. Декодирование \n2. Кодирование')
    select_mode = int(input("Выбор: "))
    if select_mode == 1: print('Вы выбрали декодирование')
    elif select_mode == 2: print('Вы выбрали кодирование.')
    else: 
        print('Неправильный выбор. Выберите 1 или 2.') 
        continue

    # Выбор способа ввода, через инпут или через файл
    print("Выберите способ ввода")
    print('1. Ручной ввод \n2. Из текстового документа')
    select_input_type = int(input('Выбор: '))
    if select_input_type == 1: print('Вы выбрали ручной ввод.')
    elif select_input_type == 2: print('Вы выбрали ввод из текстового документа.\nСледуйте дальнейшей инструкции.')
    else: 
        print('Неправильный выбор. Выберите 1 или 2.') 
        continue
    
    # вывод кодирования
    if select_mode == 2:
        if select_input_type == 1:
            message = input('Введите сообщение: ')
            d = code_1.to_morse(message)
            print("Ваш текст: ", message)
            print("Морзе: ", d)
        elif select_input_type == 2:
            print('Поместите файл с текстом в корневую папку программы.')
            s = input('Укажите название файла: ') + '.txt'
            with open(s, 'r', encoding='utf-8') as f:
                data = f.read()
            d = code_1.to_morse(data)
            print("Морзе: ", d)
            print("Текст в файле: ", data)
        save_as_txt = input('Хотите сохранить ваше сообщение в .txt файл? (y/n): ')
        if save_as_txt == "y":
            with open("code_" + str(datetime.now()), 'x') as c: # создание файла с уникальным названием
                c.write(d)
        else:
            continue

    # вывод декодирования
    elif select_mode == 1:
        if select_input_type == 1:
            message = input('Введите сообщение: ')
            print(decode.from_morse(message))
        elif select_input_type == 2:
            print('Поместите файл с текстом в корневую папку программы.')
            s = input('Укажите название файла: ') + '.txt'
            with open(s, 'r', encoding='utf-8') as f:
                data = f.read()
            print("Декодированный текст: ", decode.from_morse(data))
            print("Текст в файле: ", data)
        save_as_txt = input('Хотите сохранить ваше сообщение в .txt файл? (y/n): ')
        if save_as_txt == "y":
            with open("decode_" + str(datetime.now()), 'x') as c: # создание файла с уникальным названием
                c.write(d)
        else:
            continue



