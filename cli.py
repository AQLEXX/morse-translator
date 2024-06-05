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
                '(':'-.--.', ')':'-.--.-' 
                }
DICTIONARY_REVERSED = {value: key for key, value in DICTIONARY.items()}

import sys

while True:

    print("Выберите режим программы")
    print('1. Декодирование \n2. Кодирование')
    select_mode = int(input("Выбор: "))
    if select_mode == 1: print('Вы выбрали декодирование')
    elif select_mode == 2: print('Вы выбрали кодирование.')
    else: 
        print('Неправильный выбор. Выберите 1 или 2.') 
        continue

    print("Выберите способ ввода")
    print('1. Ручной ввод \n2. Из текстового документа')
    select_input_type = int(input('Выбор: '))
    if select_input_type == 1: print('Вы выбрали ручной ввод.')
    elif select_input_type == 2: print('Вы выбрали ввод из текстового документа.\nСледуйте дальнейшей инструкции.')
    else: 
        print('Неправильный выбор. Выберите 1 или 2.') 
        continue

