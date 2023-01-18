new_word_and_meaning = input('').lower().strip()
f = open('english_books.txt', "a")
f.write(new_word_and_meaning)
f.close()
