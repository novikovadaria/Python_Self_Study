b = 999
while 0 < b < 1000:
    alphabet = {
        "q": "й",
        "w": "ц",
        'e': 'у',
        'r': 'к',
        't': 'е',
        'y': 'н',
        'u': 'г',
        'i': 'ш',
        'o': 'щ',
        'p': 'з',
        '[': 'х',
        ']': 'ъ',
        'a': 'ф',
        's': 'ы',
        'd': 'в',
        'f': 'а',
        'g': 'п',
        'h': 'р',
        'j': 'о',
        'k': 'л',
        'l': 'д',
        ';': 'ж',
        'c': 'с',
        'z': 'я',
        'x': 'ч',
        'v': 'м',
        'b': 'и',
        'n': 'т',
        'm': 'ь',
        ',': 'б',
        '.': 'ю',
        '/': '.',
        '`': 'ё',
        '%': ' ',
        "й": "q",
        "ц": "w",
        'у': 'e',
        'к': 'r',
        'е': 't',
        'н': 'y',
        'г': 'u',
        'ш': 'i',
        'щ': 'o',
        'з': 'p',
        'х': '[',
        'ъ': ']',
        'ф': 'a',
        'ы': 's',
        'в': 'd',
        'а': 'f',
        'п': 'g',
        'р': 'h',
        'о': 'j',
        'л': 'k',
        'д': 'l',
        'ж': ';',
        'с': 'c',
        'я': 'z',
        'ч': 'x',
        'м': 'v',
        'и': 'b',
        'т': 'n',
        'ь': 'm',
        'б': ',',
        'ю': '.',
        '.': '/',
        'ё': '`',
        "(:": "🙂",
        'F': 'А',
        '-': '-'

    }

    sentence = input("")
    l_output = []
    for let in sentence:
        if let in alphabet:
            # если буква есть получаем её значение и сохраняем в переменной
            l_output.append(alphabet[let])
        else:
            l_output.append(let)
    output = "".join(l_output)
    print(output)
