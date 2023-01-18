# -------------------------------------------------------------------------------------------
# --------------------------- Самодельные хранилища -----------------------------------------
# -------------------------------------------------------------------------------------------


class BookMarkedPage():
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):  # Считаем кол-во повторов ключа
        return self.bookmarks.get(bookmark.lower(), 0)


target_bookmark = BookMarkedPage()
target_bookmark.add('Python')
target_bookmark.add('python')

print(target_bookmark.bookmarks)
print(target_bookmark['python'])


