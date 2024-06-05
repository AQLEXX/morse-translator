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
DICTIONARY_REVERSED = {value: key for key, value in DICTIONARY.items()}

import decode, code_1

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
    
    if select_mode == 2:
        if select_input_type == 1:
            message = input('Введите сообщение: ')
            print(code_1.to_morse(message))
        elif select_input_type == 2:
            print('Поместите файл с текстом в корневую папку программы.')
            s = input('Укажите название файла: ') + '.txt'
            with open(s, 'r', encoding='utf-8') as f:
                data = f.read()
            print("Морзе: ", code_1.to_morse(data))
            print("Текст в файле: ", data)


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



