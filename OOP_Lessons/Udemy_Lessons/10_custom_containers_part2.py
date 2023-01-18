# -------------------------------------------------------------------------------------------
# --------------------------- Самодельные хранилища часть 2 -----------------------------------------
# -------------------------------------------------------------------------------------------

class BookMarkedPage():
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(), 0) + 1

    # 1----------- Считаем кол-во повторов ключа -----------
    def __getitem__(self, bookmark):  
        return self.bookmarks.get(bookmark.lower(), 0)

    # 2----------- Меняем кол-во ключей ----------- 
    def __setitem__(self, bookmark, count): 
        self.bookmarks[bookmark.lower()] = count

    # 3----------- Получаем кол-во элементов ----------- 
    def __len__(self):
        return len(self.bookmarks)

    # 4----------- Итерируем ----------- 
    def __iter__(self):
        return iter(self.bookmarks)


target_bookmark = BookMarkedPage()
target_bookmark.add('Python')
target_bookmark.add('python')
target_bookmark.add('java')

# 2
target_bookmark['python'] = 100

# 3
print(len(target_bookmark))

# 1
print(target_bookmark.bookmarks)
print(target_bookmark['python'])

# 4
for bookmark in target_bookmark:
    print(bookmark)