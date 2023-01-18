import re
while True:
    sipher_keys = {
        'а': '0м',
        'б': '0ы',
        'в': '0ш',
        'г': '0е',
        'д': '0н',
        'е': '0ь',
        'ё': '0к',
        'ж': '0а',
        'з': '0+',
        'и': 'м0',
        'й': '1м',
        'к': '1ы',
        'л': '1ш',
        'м': '1е',
        'н': '1н',
        'о': '1ь',
        'п': '1к',
        'р': '1а',
        'с': 'м+',
        'т': 'ы0',
        'у': '2м',
        'ф': '2ы',
        'х': '2ш',
        'ц': '2е',
        'ч': '2н',
        'ш': '2ь',
        'щ': '2к',
        'ъ': '2а',
        'ы': 'ы+',
        'ь': 'ш0',
        'э': '3м',
        'ю': '3ы',
        'я': '3ш',
        ',': ',',
        '0м': 'а',
        '0ы': 'б',
        '0ш': 'в',
        '0е': 'г',
        '0н': 'д',
        '0ь': 'е',
        '0к': 'ё',
        '0а': 'ж',
        '0+': 'з',
        'м0': 'и',
        '1м': 'й',
        '1ы': 'к',
        '1ш': 'л',
        '1е': 'м',
        '1н': 'н',
        '1ь': 'о',
        '1к': 'п',
        '1а': 'р',
        'м+': 'с',
        'ы0': 'т',
        '2м': 'у',
        '2ы': 'ф',
        '2ш': 'х',
        '2е': 'ц',
        '2н': 'ч',
        '2ь': 'ш',
        '2к': 'щ',
        '2а': 'ъ',
        'ы+': 'ы',
        'ш0': 'ь',
        '3м': 'э',
        '3ы': 'ю',
        '3ш': 'я',
        ',': ',',
        '.': ' '

    }
    operation = input(
        'укажите номер действия:\n1.зашифровать\n2.расшифровать\n')
    if operation == '1':
        sentence = input("").lower()
        l_output = []
        for let in sentence:
            if let in sipher_keys:
                # если буква есть получаем её значение и сохраняем в переменной
                l_output.append(sipher_keys[let])
            else:
                l_output.append(let)
        output = "".join(l_output)
        print(output)
    else:
        l_output = []
        sipher_sentence = input('').lower()
        n_s = sipher_sentence.replace(' ', '  ')
        splitted_sentence = re.findall('.{%s}' % 2, n_s)
        for vow in splitted_sentence:
            if vow in sipher_keys:
                l_output.append(sipher_keys[vow])
            else:
                l_output.append(vow)
        output = ''.join(l_output)
        print(output)
