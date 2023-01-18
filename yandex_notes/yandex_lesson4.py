# ................................................Строка: последовательность букв...............................
string = 'По Борнео и Ямайке ходит слон в трусах и майке'
new_list = list(string)
new_set = set(string)
print('Список из строки: ' + str(new_list))
print('Сет из строки: ' + str(new_set))

# при создании сета:
# из строки исключены дублирующиеся символы;
# при печати элементы выводятся в случайном порядке.
# ..................................................Буквы под номерами: индексы................................
# К элементам строки (к буквам) можно обратиться по индексу, точно так же, как и к элементам списка.
# Например, по индексу [4] из строки 'Я пишу стихи на Python' будет получена буква ш.
monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])

# .........................................................Отрицательные индексы..............................
# Обратимся к элементам списка по отрицательным индексам
friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
print(friends[-3])  # Миша
print(friends[-5])  # Сергей

# То же и со строкой
monument_string = 'Я памятник себе воздвиг нерукотворный'
print(monument_string[-2])   # ы
print(monument_string[-37])  # Я

# ...........................................................Разобрать строку на слова.........................
#  метод split()
# Строку можно разделить на слова или на другие фрагменты текста — и сохранить получившиеся подстроки в список. Это делает метод split().
# Для этого метода можно указать аргумент — разделитель, по которому строка будет разбита на части.
# Разделителем может быть цифра, буква, пробел или любой набор символов.
# Например, если к строке 'молоковоз' применить метод split() с аргументом 'о' — то результатом будет список ['м', 'л', 'к', 'в', 'з'].
# При этом сам разделитель вырезается из строки.
milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)
# Будет напечатано: ['м', 'л', 'к', 'в', 'з']
counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'

# Преобразуем строку в список, а разделителем будет дефис
counter_list = counter_str.split('-')
print(counter_list)

# Создадим ещё одну строку
blok_str = 'Ночь. Улица. Фонарь. Аптека'
# Разобьём фразу по словам.
# Разделителем будет служить сочетание точки и пробела:
blok_list = blok_str.split('. ')
print(blok_list)

poem_str = 'Дама сдавала багаж'

# Применяем к строке метод split(), в скобках указываем пробел в кавычках:
words_list = poem_str.split(' ')
# Печатаем результат:
print(words_list)

message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно')

# ...................................................................Создать строку из коллекции.........................................
# метод join()
words_list = ['раз', 'два', 'три', 'четыре',
              'пять', 'вышел', 'зайчик', 'погулять']
# Метод join() "склеивает" элементы списка,
# создавая строку, в которой
# элементы исходного списка разделены текстовым символом;
# для разделения применим дефис:
new_string = '-'.join(words_list)

print(new_string)
# ....................................................................Задача 1......................................................
# Допишите код функции penult_word() так, чтобы она возвращала третье с конца слово из любой фразы, переданной в аргументе.
quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'


def penult_word(message):
    word_list = message.split()
    return word_list[-3]

# Вызовы функции готовы к работе, не изменяйте их!


# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))


# ...........................................................Задача 2...........................................
# В коде приготовлен список запросов к Анфисе queries. Необходимо определить, какие из них адресованы Анфисе, а какие — другим людям.
# Напишите функцию check_query(), которая принимает запрос как параметр, анализирует его и возвращает одну из двух строк:
# строку 'запрос к Анфисе', если запрос начинается со слова 'Анфиса',
# или строку 'запрос к кому-то ещё', если запрос начинается с любого другого слова.
# Код вызова функции и вывода результатов на экран уже написан в теле программы.
def check_query(query):
    # Допишите код тела функции
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'


# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через де

# .......................................................................Задача 3.................................................
# Анфиса научилась отличать своё имя от других. Теперь надо научить её извлекать суть запроса.
# Перепишите функцию check_query() так, чтобы при любом запросе она «отрезала» от строки имя и возвращала только запрос, без имени.
# Например, если Анфисе пришёл запрос «Толя, что это за ерунда?» — функция check_query() должна вернуть строку 'что это за ерунда?'.


def check_query(query):
    elements = query.split(', ')
    return elements[1]


# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)

# ..........................................................Задача 4..........................
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)

        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
       # Из словаря DATABASE создайте строку с помощью join();
        friends_new_string = ', '.join(DATABASE)
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = friends_new_string

        # Этот цикл больше не понадобится, удалите его

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        most_unique_cities = ', '.join(unique_cities)
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = most_unique_cities

        # Этот цикл больше не понадобится, удалите его

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

# ........................................................f-строки: переменные прямо в тексте.....................
# Выражения в f-строках
# Сложение чисел
one_hundred = 100
five_hundred = 500
print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')

# Сложение строк
one_hundred = 'сто'
five_hundred = 'пятьсот'
print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')
# Будет напечатано:
# 100 + 500 = 600
# сто + пятьсот = стопятьсот

# В f-строке можно обратиться к элементам списка по индексу:
russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
                    'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

print(f'«{russian_alphabet[-1]}» - последняя буква в алфавите.')

# Будет напечатано:
# «я» - последняя буква в алфавите.

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино'
}

song = 'Город золотой'

print(
    f'«{song}» - одна из самых известных пеcен группы «{favorite_songs[song]}».')

# Будет напечатано:
# «Город золотой» - одна из самых известных пеcен группы «Аквариум».
