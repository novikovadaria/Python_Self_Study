import webbrowser
while True:
    what_to_find = input('Что интересует?\n')
    webbrowser.open(f'https://www.google.com/search?q={what_to_find}')
