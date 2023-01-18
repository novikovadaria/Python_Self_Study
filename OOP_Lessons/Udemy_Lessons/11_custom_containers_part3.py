# -------------------------------------------------------------------------------------------
# --------------------------- Самодельные хранилища часть 3 ---------------------------------
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# ---------------------------------- Секретная память ---------------------------------------
# -------------------------------------------------------------------------------------------

class BookMarkedPage():
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):  
        return self.__bookmarks.get(bookmark.lower(), 0)


target_bookmark = BookMarkedPage()
target_bookmark.add('Python')
target_bookmark.add('python')

print(target_bookmark.bookmarks['PYTHON']) # 'BookMarkedPage' object has no attribute 'bookmarks'
print(target_bookmark.__bookmarks['PYTHON']) # AttributeError: 'BookMarkedPage' object has no attribute '__bookmarks'

# Получение скрытых данных
print(target_bookmark.__dict__) # {'_BookMarkedPage__bookmarks': {'python': 2}}