class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name

        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def display(self):
        if len(self.borrowed_books) == 0:
            books = "None"
        else:
            books = ", ".join(self.borrowed_books)

        return self.member_id + " | " + self.name + " | Borrowed: " + books
